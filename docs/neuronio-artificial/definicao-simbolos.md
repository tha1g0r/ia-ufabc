# Definição de cada símbolo

- $x_j$ ($j = 1,\dots, m$): a $j$-ésima entrada do neurônio. Na Iris, $x_1 = \text{petal length}$ e $x_2 = \text{petal width}$.

- $m$: o número de entradas. No nosso exemplo, $m = 2$.

- $w_{kj}$: o peso que liga a entrada $j$ ao neurônio $k$. Os índices são:
  - $k$: qual neurônio é (importa quando há vários, como em uma rede; com um neurônio só, $k$ é fixo);
  - $j$: qual entrada.
  
  Então $w_{k2}$ é o peso da entrada $x_2$ no neurônio $k$. O sinal de $w_{kj}$ diz se a entrada puxa a nota para cima (positivo) ou para baixo (negativo), e o módulo diz o quanto ela importa.

- $b_k$: o bias do neurônio $k$. É um número somado à soma ponderada e não multiplica nenhuma entrada.

- $u_k$: a saída do somatório, isto é, a “nota” do neurônio antes da decisão: $u_k = \sum_{j}w_{kj} \cdot x_j$. Também aparece com outros nomes, como “potencial de ativação” ou “campo local induzido”. No slide, é o que sai do $\sum$ e entra em $\varphi$.

- $\varphi(\cdot)$: a função de ativação. Recebe $u_k$ e devolve a saída final. Nas tarefas de classificação costuma ser degrau, sigmóide ou tanh, e na regressão costuma ser linear ou ReLU. Hoje usamos a degrau: $\varphi(u) = 1$ se $u \geq 0$, e $0$ caso contrário.

- $y_k$: a saída do neurônio $k$, ou seja, a resposta final: $y_k = \varphi(u_k)$. Na classificação, é a classe prevista (0 ou 1).
