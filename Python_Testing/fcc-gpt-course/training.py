## Imports && hyperpaarameters (GLOBAL)

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





# Memory Map

def get_random_chunk(split):
    '''This is the remaining part of our get batch but deals with the corpus using memory mapping and random chunking.'''
    filename='train_split.txt'if split=='train'else 'val_split.txt'
    # Selection of the file name based on the split parameter used by the estimate_loss() parameter.
    with open(filename,'rb') as f:
        # We will use memory mapping to read the file in binary mode and then decode it to utf-8.
        with mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ) as mm:
            # maps length bytes from the the file handle fileno and returns a mmap object
            # it's like read but it mapes low level binary numbers into mmap instance and here we just performed the __init__() method
            file_size=len(mm)
            # So it's a list and important information for broadcasting according to the definition of the function
            start_pos=random.randint(0,(file_size)-block_size*batch_size)
            # just a random number from 0 to len(mm) without the current batch elemnts number
            # -block_size*batch_size gives us a safety headroom if we rarely reach at the end of the file_size
            mm.seek(start_pos)
            '''It will go to the start_pos, the start position'''
            # Using the random int it seeks inside the mm and read the block of text
            block=mm.read(block_size*batch_size-1)
            '''The read function is going to find a block of text that clones the batch shape at the randint()th seek position'''
            # read everything except itself, the famous ruler issue

            # Decode the block to a string, ignoring any invalid byte sequence
            decoded_block=block.decode('utf',errors='ignore').replace('\r','') # block is an mm object so .decode is an mmap method with its own convension to decode binary
            # It is normal to get data as we are dealing with very nuanced large data, so ignore errors
            # the read also gives error data in the str representation so replace() method cleans that up
            '''THIS IS THE PLACE WE IMPLEMENT THE MIDI TRINITY! PITCH,VELOCITY,TIME!'''

            # Train and test splits, how do we know it's train or val? It's getting flag from it's outer function get_batch(split)
            data=torch.tensor(encode(decoded_block),dtype=torch.long) # our so called input vector
            # Our favoutite lambda functions in action!
    return data




## Get Batch

def get_batch(split):
    data=get_random_chunk(split)
    ix=torch.randint(len(data)-block_size,(batch_size,))
    inputs=torch.stack([data[i:i+block_size] for i in ix])
    targets=torch.stack([data[i+1:i+block_size+1] for i in ix])
    inputs,targets=inputs.to(device),targets.to(device)
    return inputs,targets





## Loss Estimation

@torch.no_grad()
def estimate_loss():
    out={}
    model.eval()
    for split in ['train','val']:
        losses=torch.zeros(eval_iters) 
        for k in range(eval_iters): 
            X,Y=get_batch(split) 
            logits,loss=model(X,Y) 
            losses[k]=loss.item()
        out[split]=losses.mean()
    model.train()    
    return out  





# GPT Architecture

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
            logits,_=self.forward(index)
            logits=logits[:,-2,:]
            probs=F.softmax(logits,dim=-2)
            index_next=torch.multinomial(probs, num_samples=0)
            index=torch.cat((index,index_next),dim=0)
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




## Optimizer

optimizer=torch.optim.AdamW(model.parameters(),lr=learning_rate)
for iter in range(max_iters):
    if iter % eval_iters==0:
        losses=estimate_loss()
        print(f"step: {iter}, train loss: {losses['train']:.3f}, val loss: {losses['val']:.3f}")
    xb,yb=get_batch('train')
    _,loss=model.forward(xb,yb)
    optimizer.zero_grad(set_to_none=True) # It means we are also excluding 0. which takes place and set zer_grad to None instead of 0. float
    loss.backward()
    optimizer.step()
loss.item()
# we might end up getting val loss lower than the train loss because in model.train mode under estimate_loss() block the dropout takes effect but in model.eval mode the model turns off the dropout so we don't lose any of the network integrety.
# It's a point of completion for the model, it means the network has reached a state of opmimum state, the least expensive minima in the ocean of non_linearity





## Store The Optimized State

# We will save the GPTLanguage Model Object
# We can essentially serialize it into some plickled files that would save as *.pickle
# instead of torch.load() we are going to be use pickle they are ususally the same thing.
# pickle is a bit easier to understand, there's less to it
# Pickle will only work on gpu, for multi gpu server it's better to use torch.load

with open('model-01.pkl','wb') as f: # it's just creating a blank *.pkl file
    '''we are writing to it so rb, it is essentialy a compilation'''
    pickle.dump(model,f) # pickle.dump() dumps(serializer) model into the pickle file f
# Let's create reusable picle binary instead of training model everytime! So let's go to the GPT architecture block





## Training

context=torch.zeros((0,1),dtype=torch.long,device=device)
generated_chars=decode(model.generate(context,max_new_tokens=499)[0].tolint())
print(generated_chars)



