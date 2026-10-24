# Backpropagation

## A intuição

Os pesos e o bias são os "botões" do neurônio. Para cada valor de $w$, o neurônio produz uma saída e essa saída gera um erro. Então o **erro $E$ é uma função do peso**: mexe em $w$, $E$ muda.

Treinar é achar o $w$ que deixa E pequeno. O gradiente $\partial E / \partial w$ é a **inclinação** dessa curva no ponto atual. Se a inclinação é positiva, aumentar $w$ aumenta o erro, então devemos diminuir $w$. Se é negativa, fazemos o contrário. Por isso treinar exige o gradiente: ele diz em que direção mexer em $w$ e com que força.

O problema é que $w$ não age direto sobre $E$. O efeito passa por uma **cadeia** $w \rightarrow s \rightarrow y \rightarrow E$, e a regra da cadeia multiplica um fator pelo elo:

- **$\partial s / \partial w_i$:** quanto a soma ponderada muda quando mexo no peso.
- **$\partial y / \partial s$:** quanto a saída do neurônio muda quando a soma muda (aqui entra a função de ativação).
- **$\partial E / \partial y$:** quanto o erro muda qando a saída muda.
