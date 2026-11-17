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
- - O1—>w^2–>O2; 
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

```Input``` is usually a big ```Vector``` ; X=[[x1],[x2],[x3],…,[xn]]

```Output``` can be so many things; for image classification a resultant vector of probabilities and we choose the biggest one, for others it can be a scalar, a boolean etc.


Rumelhart, Hinton and William’s paper “Learning Representations by Back-propagating Errors” in 1986 and re launched interest (and funding) for neural networks; Some older maths including Markova chain but being applied recently in much more novel ways and it’s not super big stretch from this to the cutting edge.

# Matrix Calculus
## [Review]
- Gradients (R^n->R^1); ```Takes in a Vector of n rows and Returns a Scalar```. I.e;

```
F(x,y)=x^2+cos(y)

[[pdF(x,y)/pdx],[pdF(X,Y)/pdy]] = [[2x],[-sin(x)]]
```

- Jacobians (R^n->R^m)
- Jacobian Chain Rule

…
