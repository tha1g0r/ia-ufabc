# Neurônio Artificial

## A ideia do neurônio

Pense em um neurônio como um **votante que dá uma nota** a cada exemplo. Cada entrada tem um peso que diz o quanto ela importa e se ela puxa a nota para cima ou para baixo. Depois a função de ativação transforma a nota em uma decisão.

Exemplo com a Iris, separando **Setosa** de **Versicolor** por duas medidas: $x_1 = \text{petal length}$ e $x_2 = \text{petal width}$. A Setosa tem pétalas pequenas, enquanto a Versicolor tem pétalas bem maiores. Então uma "nota" que cresce com o tamanho da pétala já distingue as duas.

## Formalização

Notação ([definiçao de cada símbolo](definicao-simbolos.md)):

$u_k = w_{k1} \cdot x_1 + w_{k2} \cdot x_2 + b_k$ (em geral, $u_k = \sum_{j}w_{kj} \cdot x_j + b_k$)

$y_k = \varphi(u_k)$

Para classificação com a ativação **degrau**: $\varphi(u) = 1$ se $u \geq 0$, e $\varphi(u) = 0$ caso contrário.

**Por que a fronteira é uma reta:** o neurônio troca de decisão exatamente quando $u_k = 0$, ou seja, quando $w_{k1} \cdot x_1 + w_{k2} \cdot x_2 + b_k = 0$.

No plano $(x_1, x_2)$, essa equação é uma reta. Com mais entradas ela vira um plano ou hiperplano, mas continua "reta" na ideia. Por isso um único neurônio só separa classes **linearmente separáveis**.

**Os papéis na fronteira:**

- Os pesos $w$ giram a reta (mudam a inclinação).
- O bias $b$ a desloca, sem girar. Sem bias, a reta sempre passaria pela origem.

**Exemplo numérico:** $w_{k1} = 1, w_{k2} = 1, b_k = -2.5$.

- Setosa (1.5; 0.2): $u = 1.5 + 0.2 - 2.5 = -0.8$, logo $y = \varphi(u) = 0$, pois $u < 0$.
- Versicolor (4.3; 1.3): $u = 4.3 + 1.3 - 2.5 = 3.1$, logo $y = \varphi(u) = 1$, pois $u \geq 0$.

O bias de -2.5 funciona como o limiar: o neurônio só dispara se a soma ponderada passar de 2.5.
