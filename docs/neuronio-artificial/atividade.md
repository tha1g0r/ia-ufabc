# Atividade prática

## Porta AND com um neurônio

Entradas binárias $x_1, x_2 \in {0, 1}$ e ativação degrau ($\varphi(u) = 1$ se $u \geq 0$, senão $0$). A saída desejada é:

| $\textbf{x}_\textbf{1}$ | $\textbf{x}_\textbf{2}$ | $\textbf{y}$ desejado |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Tarefa:** encontrar valores de $w_{k1}$, $w_{k2}$ e $b_k$ para que o neurônio reproduza essa tabela. Depois, confira à mão as quatro linhas, calculando $u_k$ e $y_k$ de cada uma.
> Uma reta que divide as entradas com base no $y$ desejado é $x_2 = -x_1 + 1.5 \rightarrow x_1 + x_2 -1.5 = 0$. Isso nos dá $u_k = x_1 + x_2 - 1.5$, com $w_{k1} = 1$, $w_{k2} = 1$ e $b_k = -1.5$. Vamos testar com nossos dados:
>
> - $(x_1 = 0, x_2 = 0): u_k = -1.5 \Rightarrow y = 0$
> - $(x_1 = 0, x_2 = 1): u_k = 1 - 1.5 = -0.5 \Rightarrow y = 0$
> - $(x_1 = 1, x_2 = 0): u_k = 1 - 1.5 = -0.5 \Rightarrow y = 0$
> - $(x_1 = 1, x_2 = 1): u_k = 1 + 1 - 1.5 = 0.5 \Rightarrow y = 1$

**Pergunta 1:** o ponto $(1,1)$ precisa dar $y = 1$. Escreva $u_k$ desse ponto em função de $b_k$ e a desigualdade que $b_k$ precisa satisfazer para isso. O que essa desigualdade diz: ela limita b por baixo ou por cima? Assuma $w_{k1} = w_{k2} = 1$.
> Para $(1, 1)$:
> $$u_k = w_{k1} \cdot x_1 + w{k2} \cdot x_2 + b_k = 1 + 1 + b_k = 2 + b_k$$
>Em $(1, 1)$, $y = 1$, ou seja, $u_k \geq 0$:
> $$u_k \geq 0 \rightarrow 2 + b_k \geq 0 \rightarrow b_k \geq -2$$
> Como $b_k$ precisa ser **maior ou igual** a $-2$, esse é nosso **limite inferior**.

Qual o outro limite de $b_k$?
> Agora olhamos para os pontos $(0, 1)$ e $(1, 0)$, pois compõem a reta "mais inferior" que pode dividir nossos pontos corretamente. Em ambos, $u_k = 1 + b_k$. Nesses pontos, $y = 0$, ou seja, $u_k < 0$:
> $$u_k < 0 \rightarrow 1 + b_k < 0 \rightarrow b_k < -1$$
> Como $b_k$ precisa ser **menor** que $-1$, esse é nosso **limite superior**.
>
> ---
>
> Concluímos que $b_k \in [-2, 1)$.

## Porta OR

A porta OR com entradas binárias tem esta saída desejada:

| $\textbf{x}_\textbf{1}$ | $\textbf{x}_\textbf{2}$ | $\textbf{y}$ desejado |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

**Pergunta 1:** no plano $(x_1, x_2)$, onde a reta deve passar para deixar o $(0,0)$ sozinho de um lado e os outros três pontos do outro? Descreva ou dê a equação, no formato que preferir (por exemplo, $x_2 = −x_1 + c$, com o valor de $c$ que escolher).
> A reta é a $x_2 = -x_1 + 0.5 \rightarrow x_1 + x_2 -0.5 = 0$.

**Pergunta 2:** a partir da sua reta $x_1 + x_2 − 0.5 = 0$, quais valores você atribui a $w_{k1}$, $w_{k2}$ e $b_k$? Justifique o sinal: por que escolheu essa versão da equação e não a multiplicada por $−1$?
> $w_{k1} = 1$, $w_{k2} = 1$ e $b_k = -0.5$. A versão múltiplicada por $-1$ inverteria as áreas de $y$, entregando $y = 1$ para $(x_1 = 0, x_2 = 0)$ e $y = 0$ para os outros pares.

**Pergunta 3:** confira as quatro linhas da tabela. Para cada par $(x_1, x_2)$, escreva $u_k = w_{k1} \cdot x_1 + w_{k2} \cdot x_2 + b_k$ com os números substituídos, o valor de $u_k$ e o $y_k$ resultante. Depois diga se os quatro $y_k$ coincidem com a tabela da OR.
>
> - $(x_1 = 0, x_2 = 0): u_k = -0.5 \Rightarrow y = 0$
> - $(x_1 = 0, x_2 = 1): u_k = 1 -0.5 = 0.5 \Rightarrow y = 1$
> - $(x_1 = 1, x_2 = 0): u_k = 1 -0.5 = 0.5 \Rightarrow y = 1$
> - $(x_1 = 1, x_2 = 1): u_k = 1 + 1 -0.5 = 1.5 \Rightarrow y = 1$
>
> Exatamente como a tabela OR exige.
