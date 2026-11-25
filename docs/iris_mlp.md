# MLP simples para a base IRIS

## Variáveis e formatos

*($b$ está incluso em $W$. Assim, $x_0 = 1$ está incluso em $x$)*

- *$m$ é o número de amostras*
- *$h$ é o número de neurônios na camada oculta*
- *$5$ é o número de entradas considerando $x_0$*
- *$3$ é o número de classes*

### Dados

$X^{m \times 5} \Rightarrow x^{5 \times \_}$

$y^{m \times \_} \Rightarrow {Y_\text{one\_hot}}^{m \times 3} \rightarrow {y_\text{one\_hot}}^{3 \times \_}$

### Feedforward

${W_1}^{5 \times h}$

$Z_1 = X @ W_1 \Rightarrow {Z_1}^{m \times h}$

$A_1 = \text{ReLU}(Z_1) \Rightarrow {A_1}^{m \times h}$

- Aqui integramos $h_0 = 1$ em $A_1$. Com $h' = h + 1$ e ${Ã_1} = [A_1 | 1]$:

${{Ã_1}}^{m \times h'}$

${W_2}^{h' \times 3}$

${Z_2} = {A_1}' @ W_2 \Rightarrow {Z_2}^{m \times 3}$

${A_2} = \hat{y} = \text{Softmax}(Z_2) \Rightarrow {A_2}^{m \times 3}$
