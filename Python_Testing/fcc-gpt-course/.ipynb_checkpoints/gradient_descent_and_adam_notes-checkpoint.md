# Gradient Descent, Loss Surfaces & Adam Optimization Reference

## 1. 3D Loss Surface Formulation

### Coordinate Mapping
* $x$: First learnable parameter (e.g., weight $w$).
* $y$: Second learnable parameter (e.g., bias $b$).
* $z$: Scalar Loss / Cost ($C$).
* General Surface Function:
$$z = f(x, y)$$

### Linear Regression Surface Derivation
* **Model:** $\hat{y} = wX + b$
* **Loss Function (MSE):**
$$z = C = \frac{1}{2} \sum (Y - \hat{y})^2$$
* **Example Dataset:** $(1, 2)$ and $(2, 4.5)$, mapping $w \to x$ and $b \to y$:
$$z = \frac{1}{2} \left[ (2 - (x(1) + y))^2 + (4.5 - (x(2) + y))^2 \right]$$
* **Expanded Paraboloid Equation:**
$$z = 2.5x^2 + 3xy + y^2 - 11x - 6.5y + 12.125$$

---

## 2. High-Dimensional Networks & Visualization Limits

### Direct 3D Plot Limit
* Maximum directly plottable complexity: **2 scalar learnable parameters** (e.g., 1 weight + 1 bias, or 2 weights with 0 biases).
* A 3-layer network with 2-element vectors requires $(2 \times 2) + (2 \times 2) = 8$ weights and $2 + 2 = 4$ biases ($12$ parameters + $1$ cost = **13D space**).

### Dimensionality Reduction Projections
1. **2D Slicing:** Vary 2 chosen scalar parameters on $(x, y)$; freeze all remaining weights and biases at constant values.
2. **Random Direction Projection:** Flatten all matrices and vectors into a single vector $\theta^*$, select two random direction vectors $\delta$ and $\eta$, and evaluate:
$$\theta(x, y) = \theta^* + x\delta + y\eta$$
3. **PCA Trajectory:** Project saved parameter snapshots across training epochs onto the top two principal components.

---

## 3. Gradient Descent & Calculus Equivalence

### Standard Update Rule
$$\theta_{\text{new}} = \theta_{\text{old}} - \alpha \nabla_{w,b} C$$

* $\theta$: Parameter vector (all weights and biases).
* $\alpha$: Learning rate (step size).
* $\nabla_{w,b} C$: Gradient vector of partial derivatives; slope angle $= \tan^{-1}(\nabla_{w,b} C)$.

### Continuous Gradient Flow & Euler's Method
* **Continuous Differential Equation:**
$$\frac{d\theta(t)}{dt} = -\nabla C(\theta(t))$$
* **Integral Form:**
$$\theta(T) = \theta(0) - \int_{0}^{T} \nabla C(\theta(t)) \, dt$$
* **Forward Euler Discretization ($\alpha \equiv \Delta t$):**
$$\frac{\theta(t + \Delta t) - \theta(t)}{\Delta t} = -\nabla_{w,b} C(\theta(t)) \implies \theta(t + \Delta t) = \theta(t) - \Delta t \cdot \nabla_{w,b} C(\theta(t))$$

### Mismatched Input Scaling
* Partial derivative with respect to weight:
$$\frac{\partial C}{\partial w_i} = \frac{\partial C}{\partial z} \cdot x_i$$
* Large inputs $x_i$ create steep slopes; small inputs $x_i$ create flat slopes, requiring input normalization or per-parameter adaptive learning rates ($\Delta t_i$).

---

## 4. Adam (Adaptive Moment Estimation)

### Symbol Assignments
| Symbol | Meaning | Default Value |
| :--- | :--- | :--- |
| $t$ | Training time step / iteration index | $1, 2, 3, \dots$ |
| $\theta_t$ | Parameter (individual weight or bias) at step $t$ | — |
| $g_t$ | Current gradient $\nabla_{\theta} C(\theta_{t-1})$ at step $t$ | — |
| $\alpha$ | Base learning rate ($\Delta t$) | $0.001$ |
| $m_t$ | First moment (exponential moving average of $g_t$; velocity) | $m_0 = 0$ |
| $v_t$ | Second moment (exponential moving average of $g_t^2$; steepness) | $v_0 = 0$ |
| $\beta_1$ | Decay rate for first moment ($m_t$) | $0.9$ |
| $\beta_2$ | Decay rate for second moment ($v_t$) | $0.999$ |
| $\hat{m}_t$ | Bias-corrected first moment ("jump start" velocity) | — |
| $\hat{v}_t$ | Bias-corrected second moment ("jump start" steepness) | — |
| $\epsilon$ | Numerical stability constant (prevents division by zero) | $10^{-8}$ |

### Algorithm Equations (Executed Per Parameter at Step $t$)
1. **Compute Gradient:**
$$g_t = \nabla_{\theta} C(\theta_{t-1})$$
2. **Update Biased First Moment (Momentum):**
$$m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t$$
3. **Update Biased Second Moment (Uncentered Variance):**
$$v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2$$
4. **Compute Bias-Corrected Moments (Cold-Start Fix):**
$$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \qquad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$
5. **Update Parameter:**
$$\theta_t = \theta_{t-1} - \left( \frac{\alpha}{\sqrt{\hat{v}_t} + \epsilon} \right) \hat{m}_t$$

### Bias-Correction Scaling Factors ($\beta_1 = 0.9, \beta_2 = 0.999$)
| Step ($t$) | Momentum Multiplier $\left(\frac{1}{1 - \beta_1^t}\right)$ | Steepness Multiplier $\left(\frac{1}{1 - \beta_2^t}\right)$ | Denominator Scale $\left(\sqrt{\frac{1}{1 - \beta_2^t}}\right)$ |
| :--- | :--- | :--- | :--- |
| $1$ | $10.0\times$ | $1000.0\times$ | $31.62\times$ |
| $10$ | $1.54\times$ | $100.5\times$ | $10.02\times$ |
| $50$ | $1.005\times$ | $20.5\times$ | $4.53\times$ |
| $1000$ | $1.000\times$ | $1.58\times$ | $1.26\times$ |
| $5000$ | $1.000\times$ | $1.007\times$ | $1.003\times$ |
