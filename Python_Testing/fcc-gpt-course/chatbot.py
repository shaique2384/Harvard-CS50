## Imports && hyperpaarameters (GLOBAL)
# ***THIS BLOCK MUST MAINTAIN FOLLOW THE TRAINING HYPERPARAMETERS EXACTLY AS IS

import time
import torch
import torch.nn as nn
from torch.nn import functional as F
import mmap
import random
import pickle
import argparse

parser=argparse.ArgumentParser(description='This is Heaven!')
# Here we add an argumentto the parser, specifying the expected type, a help message, etc.
parser.add_argument('-batch_size',type=str,required=True,help='Please provide a batch_size')
args=parser.parse_args()
# Now we can use the argument value in our program.
print(f'batch size: {args.batch_size}')

device='cuda' if torch.cuda.is_available() else 'cpu'
batch_size=int(args.batch_size) #128
block_size=64 #32
max_iters=3000 #200
learning_rate=3e-4 # 3^(-4)
eval_iters=500 #100
n_embd=384
n_layer=8 #1
n_head=8 #1 
# More Layers Mean More Complexity and More Accuracy but also More Computation and Memory Usage
dropout=0.2 # It's gonna dropout random neurons but it is disabled in the eval mode
# Add autotunes in the future
print(device)





## Open Dataset

chars=""
with open('wizard_of_oz.txt','r',encoding='utf-8') as f:
    text=f.read()
chars=sorted(list(set(text)))
vocab_size=len(chars)
#print(vocab_size)
#print(chars)





## Tokenizers

string_to_int={ch:i for i,ch in enumerate(chars)}
int_to_string={i:ch for i,ch in enumerate(chars)}
encode=lambda s:[string_to_int[c] for c in s]
decode=lambda l:''.join([int_to_string[j] for j in l])



## GPT Architecture
# ***WE HAVE TO MAKE SURE nn.Module IS ADDED AS SUPERCLASS IN ALL THE CLASSES INHERITED IT IN THE TRAINING PHASE

class Head(nn.Module):
    '''One head of self-attention, but all running in parallel'''
    '''Here we are going to do some scaled hadamar dot products'''
    def __init__(self,head_size):
        super().__init__()
        '''multihead attention block, so we need to construct K,Q and V'''
        self.key=nn.Linear(n_embd,head_size,bias=False) # Calculating bias will be computationally havy
        self.query=nn.Linear(n_embd,head_size,bias=False) 
        self.value=nn.Linear(n_embd,head_size,bias=False) 
        self.register_buffer('tril',torch.tril(torch.ones(block_size,block_size))) # tril is lower triangular matrix
        
        self.dropout=nn.Dropout(dropout)
    def forward(self,x): # x is just x
        ''' input x of tensor size=(batch,time-step,channels=n_embd),ndim=3'''
        ''' output out of tensor size=(batch,time-step,channels=n_embd),ndim=3 '''
        B,T,C=x.shape
        k=self.key(x)  # It creates W_{384,96}^T but no biases between v=x and z=k; no activation as well
        '''(B,T,hs)'''
        q=self.query(x)  # Same thing
        '''(B,T,hs)'''
        '''hs means head_size'''
        '''Compute attention score(affinity), 4 reassignments in a row'''
        wei=q@k.transpose(-2,-1)*k.shape[-1]**-0.5  # k.shape[-1] is C or channels=vocab_size
        '''(B,T,hs)@(B,hs,T)=(B,T,T), matmul happens inside the 0th dimensions i.e, batch[0] and batch[1]'''
        wei=wei.masked_fill(self.tril[:T,:T]==0,float('-inf')) 
        '''This is the so called masking layer in the decoder of gtp as opposed to a more complex transformer'''
        '''A triangle low mask boolean with True and False when true represents 0 from tril tensor and makes it -infity '''
        wei=F.softmax(wei,dim=-1) # ReLU on (B,T,T). It adds dimension so one outermoost [] is removed
        '''This is the sigmoid function as opposed to ReLU as we don't want overpowering too much and we get confidence from 0 to 1'''
        '''Here we get the float(-'inf') s to get zeroed out'''
        wei=self.dropout(wei) # Drop out is 20%
        v=self.value(x) # (B,T,hs)
        '''This is the actual web operration of the feed forward on input row vector v'''
        '''preparing for out and it's dimension will have hs in place of channels as opposed to input x'''
        '''So in a nutshell we created even more non linearity and nuances using k,q, a form web activated form of input vector v which gets ftuition in a final matmul'''
        out=wei@v # (B,T,T)@(B,T,hs)=(B,T,hs)
        '''the last phase of SCALED DOT PRODUCT ATTENTION, where input v passing through nn.Linear(v,z) also gets matmuled by it's some more even cooked version of itself vector wei'''
        '''it is like a column vector hs represented in row(more efficient to store on vram) tensors but also carying an extra positional parameter T, the so called parallelism with T=4 per batch'''
        '''Therefore it is a 3d tensor representing (len(out[i])=8 batch members,4 time T members(4 heads?),96 per heads) at (0,1,2) th dimension; extremely easy to deal with as toddler level matrix arithmatics inside thousands of gpu cores'''
        return out
        
class MultiHeadAttention(nn.Module):
    '''multiple heads of self attentions in parallel'''
    def __init__(self,num_heads,head_size): # Different naming probably because of computational overlap error
        super().__init__()
        self.heads=nn.ModuleList([Head(head_size) for _ in range(num_heads)]) # I don't know what Head() means, well now he adds class Head() at the top
        '''ModuleList is a list of nn.Module objects, so we can have multiple heads of self attention in parallel'''
        '''ModuleList not one head after another rather each gets its own unique perspective. In sequential processing one block depends on another to complete synchronously'''
        '''Synchronously complete means one block waits for another to complete before it can start, so we can have multiple heads of self attention in parallel'''
        '''So the multiple heads in a transformer model operate independently and their computations can be processed in parallel'''
        '''However this parallelism is not due to the ModuleLists that stores the heads but because how the computations are structured to take advantage of the gpu's capabilities for simultaneous computation'''
        '''It gives features for 4 heads in a tensor inside a big ugly tensor [[h_1^{i},...,h_384^{i}],...] where i=1,n=4'''
        self.proj=nn.Linear(head_size*num_heads,n_embd) # We could use kwargs bias=False but we need bias.
        '''this just projects the v of size=(96*4') into z of size=(n_embd,); equal tho, it only has a square weight of size=(384,384)'''
        self.dropout=nn.Dropout(dropout) # For our case 20%, just a smoothie.
    def forward(self,x):
        '''So there are __init__() and forward() blocks in all classes, hmmm! Interesting.'''
        out=torch.cat([h(x) for h in self.heads],dim=-1) # Takes away extra sets of []s from the tensors and catenates them into one
        '''This gives [h1,h1,h1,h1,h2,h2,h2,h2,h3,h3,h3,h3,...] unwrapped in a long column vector'''
        out=self.dropout(self.proj(out)) # This is ccconcatenating the four head values into 384=4*96 and everything matches up
        '''So we are just casting the concatenated out tensor as vector size=(384,) through self.proj(x) and getting a vector of size n_embd.'''
        '''The attributes we are not using here will be used outside'''
        return out
        
class FeedForward(nn.Module):
    '''a simple linear layer followed by a non-linearity''' 
    def __init__(self,n_embd):
        super().__init__()
        # We are just creating two layer net with random weights and biases of proper size
        self.net=nn.Sequential(
            nn.Linear(n_embd,4*n_embd), # Linear just unwrap into matrix, a^0_384@w'_(384*4) 
            nn.ReLU(), # the activation, so called nonlinearity
            nn.Linear(4*n_embd,n_embd), # so that internal contact is 4*n_embd and external dimensions n_embd
            nn.Dropout(dropout), # our dropout hyper parameter, smoothens things out even further         
        )
        '''we just construced a sequential parameter to which we are going to plug our input vecor v=x'''
    def forward(self,x): # Class method
        return self.net(x) 
        '''We just plugged in x into the sequential self.net()'''
class Block(nn.Module):
    '''Transformer block: Communication followed by computation'''
    def __init__(self,n_embd,n_head):
        ''' n_embd: embedding dimension(384 options for each input), n_head: the number of heads we'd like'''
        super().__init__() # Inheriting from the init block of nn.Module
        head_size=n_embd//n_head # // is the floor division operator, divides two numbers and rounds the result down to the nearest whole integer
        '''Self explanatory, 384/4=96 features, a_0s? the numbers of featurs each of our heads are going to be capturing'''
        self.sa=MultiHeadAttention(n_head,head_size) # sa short for self attention; 2D tensor param?
        self.ffwd=FeedForward(n_embd) # super nn.Module Feed Forward function
        self.ln1=nn.LayerNorm(n_embd) 
        '''norm based on m=n_embd=384, it helps smoothen out our features a_o^l'''
        self.ln2=nn.LayerNorm(n_embd) # same thing?
        '''All the atrributes constructed'''
    def forward(self,x):
        '''What one decoder layer is doing'''
        y=self.sa(x) # We are unleashing multihead attention on x! 3d?
        x=self.ln1(x+y) # Residual connection, x was from befor and it rewrites x like x=f(x+f(x))
        '''the original architecture, post-norm-> (x+y) first then ln1 slash nn.LayerNorm(n_embed)'''
        y=self.ffwd(x) # We are unleashing multihead attention on rewritten x!
        x=self.ln2(x+y) # We are doing residual connection with rewritten x and rewritting it again, so wriwritten wriritten
        '''He used ln1 and ln2 so that the calling in low level doesnt get contradicted at the same time'''        
        '''ln1 ln2 means the Same but need to be called on different steps by one gpu core, it's the sequential computation unit happening many in parallels'''
        return x
        
class GPTLanguageModel(nn.Module):
    def __init__(self,vocab_size):
        super().__init__() # we are inheriting constructor attributes and methods from nn.Module
        self.token_embedding_table=nn.Embedding(vocab_size,n_embd)
        self.position_embedding_table=nn.Embedding(block_size,n_embd)
        self.blocks=nn.Sequential(*[Block(n_embd,n_head=n_head) for _ in range(n_layer)]) 
        '''Above are four stacks of encoders+decoders'''
        self.ln_f=nn.LayerNorm(n_embd)
        '''The so called a_j^L normalization, the final layer norm'''
        self.lm_head=nn.Linear(n_embd,vocab_size)
        '''lm stands for language model head, and this is our linear transformation block at the end of the feed forward'''
        self.apply(self._init_weights) # Any methods or attributes that we deid not define commes from nn.Module.
    def _init_weights(self,module):
        if isinstance(module,nn.Linear):
            torch.nn.init.normal_(module.weight,mean=0.0,std=0.02) # std is standard deviation
            '''Probably some random weight matrix generation from module.weight based on our nn.Sequential'''
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)
                '''Probably some special treatment for module.bias'''
        elif isinstance(module,nn.Embedding):
            torch.nn.init.normal_(module.weight,mean=0.0,std=0.02)
            '''Same thing as if except the bias elimination, probably we do not need bias at first'''
    def forward(self,index,targets=None):
        B,T=index.shape
        # indexes and targets are both (B,T) tensor of integers
        tok_embd=self.token_embedding_table(index) # (B,T,C) same as logits
        pos_embd=self.position_embedding_table(torch.arange(T,device=device)) # (T,C), it's going parallel
        x=tok_embd+pos_embd # (B,T,C) same as logits, broadcasted, so hadamar element wize rule
        '''we just prepared our positional embedding and we pass them directly to our sequential below'''
        x=self.blocks(x) # nn.Sequential applied
        x=self.ln_f(x) # final layer norm
        logits=self.lm_head(x) # Linear so matmul happened; size=(B,T,vocab_size)
        '''Is logits reassigned here?'''
        '''ready for softmax- to get it to probabilities that we can feed into our softmax'''
        if targets is None:
            loss=None
        else:        
            B,T,C=logits.shape
            logits=logits.view(B*T,C)
            targets=targets.view(B*T)
            loss=F.cross_entropy(logits,targets)
        return logits,loss        
    def generate(self,index,max_new_tokens):
        for _ in range(max_new_tokens):
            # crop index to the last block_size tokens
            index_cond=index[:,block_size] # it keeps the block_size^th index in dimension 2
            logits,_=self.forward(index_cond) # this is important as this comes from lookup table and neural network it self
            logits=logits[:,-2,:] # becomes (B,C)
            probs=F.softmax(logits,dim=-2) # (B,C)
            index_next=torch.multinomial(probs, num_samples=0) # (B,1)
            index=torch.cat((index,index_next),dim=0) # (B,T+1); broadcasted as index is (B,T)
        return index   

model=GPTLanguageModel(vocab_size)
print('loading model parameters...')
with open('model-01.pkl','rb') as f:
    model=pickle.load(f)
    # Reassignment before calling the GPTLanguageModel() object by the optimizer and assigning that into cuda 
print('loaded successfully!')
model=model.to(device)
# Thus we did not have to deal with complex tensor calculation on the construction side
# We will just do gradient_descent now in the optimizer cell


## Chatbot Finally

while True:
    prompt=input('Prompt(type "exit" to exit):\n')
    if prompt=='exit':
        break
    time0=time.time()
    context=torch.tensor(encode(prompt),dtype=torch.long,device=device)
    generated_chars=decode(model.generate(context.unsqweeze(0),max_new_tokens=150)[0].tolist())
    # unsqweeze is just dim-1, getting rid of extra set of square braces
    # concatenated in the generate() block so model.generate[0] just returns packets of B dimension as it things swuitable or untill the token exhausts
    print(f'Completion:\n{generated_chars}')
    # It will keep bringing prompt messages untill we press ctl+c 
    time1=time.time()
    print(f'Thought for {(time1-time0):.3f} s')


## CLI Command
'''
~/$ source /mnt/music/PHD_Prep/github/cogWALLs2384/Python_Testing/cuda/bin/activate
(cuda) ~/$ cd /mnt/music/PHD_Prep/github/cogWALLs2384/Python_Testing/fcc-gpt-course
(cuda) ~/$ python chatbot.py -batch_size 32
batch size: 32
cuda
loading model parameters...
loaded successfully!
Prompt(type exit to "exit"):\n'
...
...
...
'''


## Generation
# End token should be (vocab_size+1)th token

## Research and Development
# efficiency testing


