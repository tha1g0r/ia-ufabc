# The Math

## Network Architecture

Rede neural de 2 camadas:

1. Camada 0 (camada de entrada): 784 unidades – cada um 1 dos 784 pixels mapeia para um nó.
2. 1ª Camada (camada oculta): 10 unidades.
3. 2ª Camada (camada de saída): 10 unidades – cada uma corresponde a um dígito que pode ser previsto.

## Feedforward Propagation

1. Camada de entrada sem processamento: $$A^{[0]} = x$$

2. Primeira camada não ativada: $$Z^{[1]} = w^{[1]} A^{[0]} + b^{[1]}$$

3. Função de ativação na primeira camada: $$A^{[1]} = g(Z^{[1]}) = \text{ReLU}(Z^{[1]})$$ $$\text{ReLU}(x) = \begin{cases} x, & \text{se } x>0 \\ 0, & \text{se } x \le 0 \end{cases}$$

4. Segunda camada não ativada: $$Z^{[2]} = w^{[2]} A^{[1]} + b^{[2]}$$

5. Função de ativação: $$A^{[2]} = \text{softmax}(Z^{[2]})$$

    - **Softmax** é uma função que atribui uma probabilidade para cada classe de saída.

## Backpropagation

Erro da segunda camada: ${dZ}^{[2]} = A^{[2]} - Y$
$${dw}^{[2]} = \frac{1}{m} {dZ}^{[2]} {A^{[1]}}^T$$
$${db}^{[2]} = \frac{1}{m} \sum{{dZ}^{[2]}}$$
$${dz}^{[1]} = {w^{[2]}}^T {dz}^{[2]} \cdot g'(Z^{[1]})$$
$${dw}^{[1]} = \frac{1}{m} {dZ}^{[1]} X^T$$
$${db}^{[1]} = \frac{1}{m} \sum{{dZ}^{[1]}}$$
