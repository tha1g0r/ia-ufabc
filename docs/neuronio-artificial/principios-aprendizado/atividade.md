# Atividade

## Deduza a regra do bias

**obs:** uso da soma ponderada mas com novos índices (neurônio $j$, entrada $i$), ou seja, $u_j = \sum_{i} w_{ij} \cdot x_i + b_j$.

A regra dos pesos é: $\Delta w_{ij} = \eta (y_j - \hat{y}_j) \cdot x_i$.

1. Escreva a regra do bias, $\Delta b_j$.
    > $b_j$ é um peso $w_{0j}$ cuja entrada $x_0 = 1$. Assumindo $i = 0$, $\Delta w_{0j} = \eta (y_j - \hat{y}_j) \cdot x_0 \rightarrow \Delta b_j = \eta (y_j - \hat{y}_j)$.

2. Justifique em uma ou duas frases por que ela tem essa forma, com base no que você entendeu sobre a regra dos pesos.
    > A resposta acima já abrange esse item.
3. Confira se o sinal de $\Delta b_j$ faz sentido nos casos (a) $y_j = 1$ e $\hat{y}_j = 0$, e (b) $y_j = 0$ e $\hat{y}_j = 1$.
    > Para $y_j = 1$ e $\hat{y}_j = 0$:
    >
    > $\Delta b_j = \eta (1 - 0) = \eta$. Como $\eta > 0$, $\Delta b_j > 0$.
    >
    > Com $\Delta b_j > 0$, $u_j$ cresce. Isso faz sentido pois a previsão do modelo foi mais "baixo" do que o rótulo real.
    >
    > Para $y_j = 0$ e $\hat{y}_j = 1$:
    >
    > $\Delta b_j = \eta (0 - 1) = -\eta$. Como $\eta > 0$, $\Delta b_j < 0$.
    >
    > Com $\Delta b_j < 0$, $u_j$ diminui. Isso faz sentido pois a previsão do modelo foi mais "alto" do que o rótulo real.

## Um passo de atualização

Vamos usar a primeira amostra real da Iris, uma **Setosa**:

- $x_1$ = comprimento da pétala = $1.4 \text{ cm}$
- $x_2$ = largura da pétala = $0.2 \text{ cm}$
- rótulo: $y_j = 1$ (Setosa; não-Setosa seria $0$)

Use o degrau $\hat{y}_j = 1$ se $u_j \geq 0$, e $\hat{y}_j = 0$ se $u_j < 0$, com $u_j = w_{1j}·x_1 + w_{2j} \cdot x_2 + b_j$.

**Sua tarefa:**

1. Escolha $w_{1j}$, $w_{2j}$, $b_j$ e $\eta > 0$ (para a atualização ser mais interessante, escolha valores em que o neurônio erre: $u_j < 0$)
    > $u_j < 0 \rightarrow 1.4 \cdot w_{1j} + 0.2 \cdot w_{2j} + b_j < 0$.
    >
    > Vamos assumir $w_{1j} = 1$, $w_{2j} = 1$ e $b_j = -1.7$ (esses valores respeitam a condição acima).
    >
    > $\eta > 0$ é arbitrário para números positivos. Vamos utilizar $\eta = 0.1$.

2. Calcule $u_j$, $\hat{y}_j$ e o erro $y_j − \hat{y}_j$.
    > $u_j = 1.4 + 0.2 - 1.7 = -0.1$. Como $u_j < 0$, $\hat{y}_j = 0$.
    >
    > O erro é $\text{error} = y_j - \hat{y}_j = 1 - 0 = 1$.

3. Calcule $\Delta w_{1j}$, $\Delta w_{2j}$ e $\Delta b_j$.
    > $\Delta w_{1j} = \eta \cdot \text{error} \cdot x_1 = 0.1 \cdot 1 \cdot 1.4 = 0.14$
    >
    > $\Delta w_{2j} = \eta \cdot \text{error} \cdot x_2 = 0.1 \cdot 1 \cdot 0.2 = 0.02$
    >
    > $\Delta b_j = \eta \cdot \text{error} = 0.1 \cdot 1 = 0.1$

4. Calcule os novos valores de $w_{1j}$, $w_{2j}$ e $b_j$.
    > $\Delta = \text{final} - \text{inicial} \rightarrow \text{final} = \text{inicial} + \Delta$
    >
    > $w_{1j} = 1 + 0.14 = 1.14$
    >
    > $w_{2j} = 1 + 0.02 = 1.02$
    >
    > $b_j = -1.7 + 0.1 = -1.6$
    >
    > Para esses novos valores:
    >
    > $u_j = 1.14 \cdot 1.4 + 1.02 \cdot 0.2 - 1.6 = 0.2$. Como $u_j \geq 0$, $\hat{y}_j = 1$ e o modelo prevê corretamente.

**Uma checagem que vale conhecer**. O $u_j$ subiu de $−0.1$ para $0.2$, ou seja, $+0.3$. Esse valor sai direto da regra: cada termo contribui com $\eta \cdot \text{error} \cdot (\text{entrada})^2$, e o bias contribui com $\eta \cdot \text{error} \cdot 1^2$. Somando, $0.1 \cdot (1.4^2 + 0.2^2 + 1) = 0.1 \cdot 3 = 0.3$. Isso mostra que a regra empurra o $u_j$ na direção certa, sempre.

**Um cuidado:** o neurônio corrigiu em um passo porque o erro de $u_j$ era pequeno ($−0.1$) e o $\eta$ era razoável. Em geral, um passo só move o $u_j$ na direção certa e pode não bastar para cruzar o limiar, como vimos antes.

### Segunda amostra

Os dados desta etapa:

- **Amostra:** a primeira Versicolor da Iris (não-Setosa), com $x_1 = \text{comprimento da pétala} = 4.7 \text{ cm}$, $x_2 = \text{largura da pétala} = 1.4 \text{ cm}$ e rótulo $y_j = 0$.
- **Pesos de partida:** são os que você obteve no fim da atividade anterior, $w_{1j} = 1.14$, $w_{2j} = 1.02$ e $b_j = −1.6$.
- **$\eta$:** continua $0.1$.
- **Degrau:** $\hat{y}_j = 1$ se $u_j \geq 0$ e $\hat{y}_j = 0$ se $u_j < 0$.

Antes de calcular, faça uma previsão: com esses pesos, você espera que o neurônio acerte ou erre essa amostra? Se errar, em qual dos casos, (a) ou (b)?
> Com esses pesos conseguimos $u_j > 0$ para os valores de entrada pequenos de uma Setosa. As entradas de uma Versicolor são maiores. Com $x_i$ maiores, o valor de $u_j$ será ainda maior, contribuindo para $\hat{y}_j = 1$, o que fará com que o modelo erre.
>
> Os valores de entrada de uma Versícolor são muito maiores do que de uma Setosa. Como temos um passo ($\eta$) pequeno, acredito que uma atualização não será o seficiente para cobrir essa diferença e fazer com que o modelo classifique $\hat{y}_j = 0$.

1. Calcule $u_j$, $\hat{y}_j$ e o erro $y_j − \hat{y}_j$.
    > $u_j = w_{1j} x_1 + w_{2j} x_2 + b_j = 1.14 \cdot 4.7 + 1.02 \cdot 1.4 - 1.6 = 5.186$
    >
    > $u_j > 0 \Rightarrow \hat{y}_j = 1$
    >
    > $\text{error} = y_j − \hat{y}_j = 0 - 1 = -1$

2. Calcule $\Delta w_{1j}$, $\Delta w_{2j}$ e $\Delta b_j$.
    > $\Delta w_{1j} = \eta \cdot \text{error} \cdot x_1 = 0.1 \cdot (-1) \cdot 4.7 = -0.47$
    >
    > $\Delta w_{2j} = \eta \cdot \text{error} \cdot x_2 = 0.1 \cdot (-1) \cdot 1.4 = -0.14$
    >
    > $\Delta b_j = \eta \cdot \text{error} = 0.1 \cdot (-1) = -0.1$

3. Calcule os novos $w_{1j}$, $w_{2j}$ e $b_j$.
    > $w_{1j}' = w_{1j} + \Delta w_{1j} = 1.14 - 0.47 = 0.67$
    >
    > $w_{2j}' = w_{2j} + \Delta w_{2j} = 1.02 - 0.14 = 0.88$
    >
    > $b_j' = b_j + \Delta b_j = -1.6 - 0.1 = -1.7$

4. Recalcule $u_j$ com os novos pesos e diga se a previsão passou a estar correta.
    > $u_j' = w_{1j}' x_1 + w_{2j}' x_2 + b_j' = 0.67 \cdot 4.7 + 0.88 \cdot 1.4 - 1.7 = 2.681$
    >
    > $u_j' > 0 \Rightarrow \hat{y}_j' = 1$
    >
    > A previsão do modelo ainda é errada, mas dessa vez, chegamos mais perto de termos $u_j < 0$.

**Checagem do tamanho do passo**. O $u_j$ caiu $2.505$, de $5.186$ para $2.681$. Esse valor sai da regra: $\Delta u_j = \eta \cdot \text{error} \cdot ({x_1}^2 + {x_2}^2 + 1) = 0,1 \cdot (−1) \cdot (22.09 + 1.96 + 1) = −2.505$. Isso confirma sua leitura de que uma atualização não basta. Repetindo o passo só com essa amostra, seriam necessárias três atualizações até $u_j < 0$.
