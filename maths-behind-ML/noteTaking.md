# Agenda

- Big Picture
- Multivariable Calculus Review
- Neuron as Function
- Jacobians & NNs
- Gradient Descent
- Back Propagation
- BP as Matrix Calculus 

*```All Matrix Calculus Is Multivariable Calculus```
*```Not All Multivariable Calculus is Matrix Calculus```


# Notations

- m = size of train set
- n = amt. of input vars
- L = amt. of layers in NN; 
- - .l = specific layer
- W^l = weight(s), l = layer going into; ```layer1->layer2``` vs ```layer(n-1)—>layer(n)```
- - —>w^2–>O2; 
- - O(n-1)—>w^n=On; 
- - b^l = bias for layer l; for the above case bias is for l2 and ln
- Xi = single input variable; each of our training samples have one input variables


# Big Picture

- NNs as functions; a big ```Fancy Function``` made up of small ones
- Just a big calculus problem
- - All about minimizing the cost function; some form of d(S(cost)/d(S(W)); we tweak the parameters and get finalized the model.
- Gradient descent gives us the minima of the gradient in a set of dimensions; ```Solid Geometry``` is the key, hence topology and manifolds.

If the curve of the cost function;

    |           |
    |           |
    |           |
    \           /
     \         /
      (       )
       \_   _/       
         -.-
```minima    * ```

```Input``` is usually a big ```Vector``` ; X=[[x1],[x2],[x3],…,[xn]] or,
$$
\vec{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ \vdots \\ x_n \end{bmatrix}
$$

```Output``` can be so many things; for image classification a resultant vector of probabilities and we choose the biggest one, for others it can be a scalar, a boolean etc.


Rumelhart, Hinton and William’s paper “Learning Representations by Back-propagating Errors” in 1986 and re launched interest (and funding) for neural networks; Some older maths including Markova chain but being applied recently in much more novel ways and it’s not super big stretch from this to the cutting edge.

# Matrix Calculus
## [Review]
- Gradients ( $\mathbb{R}^n \rightarrow  \mathbb{R}^1$ ); ```Takes in a Vector of n rows and Returns a Scalar```. I.e;

- $F(x,y)=x^2+cos(y)$
- $\partial F_{(x,y)}/\partial x = \begin{bmatrix} 2x \\ -sin(x) \end{bmatrix}$
- Jacobians ( $\mathbb{R}^n \rightarrow  \mathbb{R}^{n|m}$ )
- Jacobian Chain Rule 

# Neuron
## [Feed Forward]

- Inputs are dot product.
- Visual example;
$
\begin{bmatrix}
x_1 & - & w_1 & \rightarrow \\
x_2 & - & w_2 & \rightarrow \\
x_3 & - & w_3 & \rightarrow & [\mathbb{N}] \\
\vdots & - & \vdots & \ddots \\
x_n & --- & w_n & \rightarrow \end{bmatrix} 
$
- Our neuron will take the Weighted Sum; $\sigma( \sum_{k=1}^{n} x_iw_i + b)$ 
- The symbol $b$ stands for bias, a scalar that is added to the sum to tweak the output.
- The $\sigma$ at the start represents the sigmoid function or activation function.
- The sigmoid function is a little more old now, not so popular, rectified linear linear unit or relu is more popular these days and a neural network with no nonlinear activation can be proven to be equal to linear regression.
- Exact Mathematical Definition:
$$
f(x)=\begin{cases}0&\text{if }x<0\\
x&\text{if }x\ge0\end{cases}
$$
- Compact Maximum Form:
$$
f(x)=\max(0,x)
$$
- This is one kind of exponentiate function like the torch.exp(tensor) but keeping x as is(not shoving inside $e^x$)
- It's like a rectifier, refering to amplification, rectifying all the negative values of x. tensor.mask() which takes in boolean can be helpful where we just put a conditional where tensor[i]=>0, and it should take the positive tensor[i] values for tensor.rand(m,n,...).
- This is basically, an element wise multiplication or dot product between the matrix containing our inputs and weighted sum. For example;
- If $\vec{x}=\begin{bmatrix}x_1\\x_2\\x_3\\\vdots\\x_n\end{bmatrix}\text{, }\vec{w}=\begin{bmatrix}w_1\\w_2\\w_3\\\vdots\\w_n\end{bmatrix}
\text{, Sigmoid Activation Function; }
\vec{x}^T\cdot\vec{w} \text{ or, } {\begin{bmatrix}x_1\\x_2\\x_3\\\vdots\\x_n\end{bmatrix}}^T\cdot\begin{bmatrix}w_1\\w_2\\w_3\\\vdots\\w_n\end{bmatrix}$
- We can simplify the sigmoid function from weighted sum to matrix dot products;
$$\sigma({\vec{X}}^T\cdot\vec{W}+b)$$
- The function occurs in two stages;
  1. First we assign $({\vec{X}}^T\cdot\vec{W}+b)$ to variable $\mathbf{Z}$
  2. Then we put $\mathbf{Z}$ into the sigmoid function $\sigma{()}$ and assign to activation $\mathbf{a}$ so that $\mathbf{a}=\sigma{(\mathbf{Z})}$
- We will encounter more superscripts and subscripts when we will deal with multiple neurons.
- The sigmoid function takes in a vector and returns a scalar because ${\vec{X}}^T\cdot\vec{W}$ gives a scalar. It collapses the input vector $\vec{X}$ into rank 0. We end up with only one unit vector where direction becomes redundant; therefore a scalar. 
- That's all it is, that's all a single neuron or node does.
# Layer Of NN
- Weight representation for a layer of neurons|nodes is not as straight forward. Multiple weights are involved as strings to connect each $x_i$ with nwurons|nodes of one layer.
- To locate the weight in the context of the totality the notation $\mathbf{W}_{jk}^l$ is used. 
  - It denotes a single weight of such system where $l$ is the index of the layer $W$ is going to, $j$ is the index of the neuron in $layer_l$ it is going to and $k$ is the index of the node in layer $layer_{(l-1)}$ 
- The index of the node the weight is going to implies as follows;
$$
\mathbf{W}_{jk}^l\implies j^{th}row,l^{th}col
$$
- Biases $b$ are usually same for the nodes in the same layer and denoted by $b^l$ where $l$ is the index of the layer as stated before; it usually equals to a scalar.
- If bias for different nodes are different they are written as $b^l_i$ where $i$ is the index of the node in $layer_l$.
- Each node in the first layer receives the wighted sum from all the $x_i$ of $vec{v}$ and their weights. 
- Connecting $n$ number of inputs with $m$ number of nodes in layer $l=1$ will require $m\times n$ number of $\mathbf{W}_{i0}^1$ weights and therefore $m$ number of weighted sums for that many nodes.
- So for node $\mathbf{N}_j$ activation from input when $k$ is ommitted as $k=0$;
$$
a_j=\sigma({\begin{bmatrix}x_1\\x_2\\x_3\\\vdots\\x_n\end{bmatrix}}^T\cdot\begin{bmatrix}w_{j1}^1\\w_{j2}^1\\w_{j3}^1\\\vdots\\w_{jn}^1\end{bmatrix}+b^1)
$$
- The output from layer l=1 is a vector $\mathbb{R}^m$ containing m number of outputs;
$$
\begin{bmatrix}a_1^1\\a_1^1\\a_1^1\\\vdots\\a_1^1\end{bmatrix}=\begin{bmatrix}\sigma({\begin{bmatrix}x_1\\x_2\\x_3\\\vdots\\x_n\end{bmatrix}}^T\cdot\begin{bmatrix}w_{11}^1\\w_{12}^1\\w_{13}^1\\\vdots\\w_{1n}^1\end{bmatrix}+b^1)\\\sigma({\begin{bmatrix}x_1\\x_2\\x_3\\\vdots\\x_n\end{bmatrix}}^T\cdot\begin{bmatrix}w_{21}^1\\w_{22}^1\\w_{23}^1\\\vdots\\w_{2n}^1\end{bmatrix}+b^1)\\\sigma({\begin{bmatrix}x_1\\x_2\\x_3\\\vdots\\x_n\end{bmatrix}}^T\cdot\begin{bmatrix}w_{31}^1\\w_{32}^1\\w_{33}^1\\\vdots\\w_{3n}^1\end{bmatrix}+b^1)\\\vdots\\\vdots\\\sigma({\begin{bmatrix}x_1\\x_2\\x_3\\\vdots\\x_n\end{bmatrix}}^T\cdot\begin{bmatrix}w_{m1}^1\\w_{m2}^1\\w_{m3}^1\\\vdots\\w_{mn}^1\end{bmatrix}+b^1)\\ \end{bmatrix}
$$
- Cleaner representation of activation vector from $m$ number of $\mathbf{N}$ neurons, the computation unit of the model;
$$
\begin{bmatrix}a_1^1\\a_2^1\\a_3^1\\\vdots\\a_m^1\end{bmatrix}=\begin{bmatrix}\sigma{(\vec{X}^T\cdot\vec{W}_1^1+b^1)}\\\sigma{(\vec{X}^T\cdot\vec{W}_2^1+b^1)}\\\sigma{(\vec{X}^T\cdot\vec{W}_3^1+b^1)}\\\vdots\\\sigma{(\vec{X}^T\cdot\vec{W}_m^1+b^1)}\\\end{bmatrix}
$$

- The program becomes a recursive operation of $\sigma{(W^l\cdot A^{l-1}+b^l)}$ where the product is a matrix multiplication like linearly transforming a vector where order matters.

- Also all the neurons of $layer_l$ contain activations from previous neurons of $layer_{l-1}$ represented as a vector $\vec{A}^{l-1}$ of $\mathbb{R}^{m_{l-1}}$ shape. It Goes through the neuron activation from $\vec{A}^{l-1}$ to $\vec{A}^{l}$ as the output of $layer_l$. 
- All the weighted sums can be cleanly represented by a linear transformation using a $W^l$ matrix of $(m^l\times m^{l-1})$ shape containing all the weights between $layer_l,layer_{l-1}$ in proper order so that the activation by $\mathbf{N}_1$ can be represented as;
$$a_1^l=\sigma(\sum_{k=1}^{m^{l-1}}a_k^{l-1}\cdot w_{1k}^l +b^l)$$
- This computation can be achieved with the matrix below;
$$
W^l=\begin{bmatrix} w_{11}^l & w_{12}^l & w_{13}^l & \cdots & w_{1m^{l-1}}^l \\
w_{21}^l & w_{22}^l & w_{23}^l & \cdots & w_{2m^{l-1}}^l \\
w_{31}^l & w_{32}^l & w_{33}^l & \cdots & w_{3m^{l-1}}^l \\ 
\vdots & \vdots & \vdots & \ddots & \vdots \\
w_{m^l1}^l & w_{m^l2}^l & w_{m^l3}^l & \cdots & w_{m^lm^{l-1}}^l \end{bmatrix}
$$
- Multiplying it with the input vector $\vec{A}^{l-1}$ of $layer_l$ we get vecor with different dimension as bellow;
$$
\begin{bmatrix} w_{11}^l & w_{12}^l & w_{13}^l & \cdots & w_{1m^{l-1}}^l \\
w_{21}^l & w_{22}^l & w_{23}^l & \cdots & w_{2m^{l-1}}^l \\
w_{31}^l & w_{32}^l & w_{33}^l & \cdots & w_{3m^{l-1}}^l \\ 
\vdots & \vdots & \vdots & \ddots & \vdots \\
w_{m^l1}^l & w_{m^l2}^l & w_{m^l3}^l & \cdots & w_{m^lm^{l-1}}^l \end{bmatrix}\cdot\begin{bmatrix}a_1^{l-1}\\a_2^{l-1}\\a_3^{l-1}\\\vdots\\a_{m^{l-1}}^{l-1}\end{bmatrix}\rightarrow\mathbb{R}^{m^l}
$$
- Now adding each member of matrix dot product with $b^l$ and then executing each with sigmoid function we get $\vec{A}^{l}$ as the input for neuron $layer_{l+1}$ as below;
$$
\sigma(\begin{bmatrix} w_{11}^l & w_{12}^l & w_{13}^l & \cdots & w_{1m^{l-1}}^l \\
w_{21}^l & w_{22}^l & w_{23}^l & \cdots & w_{2m^{l-1}}^l \\
w_{31}^l & w_{32}^l & w_{33}^l & \cdots & w_{3m^{l-1}}^l \\ 
\vdots & \vdots & \vdots & \ddots & \vdots \\
w_{m^l1}^l & w_{m^l2}^l & w_{m^l3}^l & \cdots & w_{m^lm^{l-1}}^l \end{bmatrix}\cdot\begin{bmatrix}a_1^{l-1}\\a_2^{l-1}\\a_3^{l-1}\\\vdots\\a_{m^{l-1}}^{l-1}\end{bmatrix}+b^l)=\begin{bmatrix}a_1^l\\a_2^l\\a_3^l\\\vdots\\a_{m^l}^l\end{bmatrix}
$$

- So ultimately each activation is a linear transform from a vector $\vec{A}^{l-1}$ to $\vec{A}^{l}$ or $\mathbb{R}^{m_{l-1}}\rightarrow\mathbb{R}^{m_{l}}$ and we can simplify even more;
$$
\sigma(W^l\cdot\vec{A}^{l-1}+b^l)=\vec{A}^{l}
$$
- This is a feed-forward operation and we will get a very crude final output but after performing back propagation to timprove the weights and then repeating the cycle couple of times we will get a better performing model.

# Motivation & Cost Function
## [Back Propagation]
- We will explore how we can lower the cost of our final output, minimize errors and improve the accuracy of our model by changing the weights and biases in our entire algorythm.
- We will be going back through the network and discover how each of the weights and biases affect the total cost; this is where the curve and noncoplaner surfaces and calculus will provide guidelines for maximas and minimas of perfeomances; manifold can be useful as well.

# JACOBIANS AND NN'S
- Simple Model
#### MSE(Mean Square Error, A Cost Function):
- 
- Calculating Derrivatives 
- Gradient Descent

Do $\begin{bmatrix} a_1x_1 & a_1x_2\\a_2x_1 & a_2x_2\\a_3x_1 & a_3x_2\\\end{bmatrix}$ and 
$\begin{bmatrix} a_1 \begin{bmatrix} x_1 & x_2 \end{bmatrix}\\a_2\begin{bmatrix} x_1 & x_2 \end{bmatrix}\\a_3\begin{bmatrix} x_1 & x_2 \end{bmatrix}\end{bmatrix}$ mean same? Yes