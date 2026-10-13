# Modelos clássicos

## Principais modelos

**Naive-Bayes.** Para uma amostra nova, calcula a probabilidade de cada classe dado os valores das variáveis e escolhe a classe mais provável. Ele é "ingênuo" porque assume que as variáveis são independentes entre si (sem correlação) e que cada uma segue uma distribuição normal.

- O modelo **não verifica** se a variável é normal. Ele **assume** que é. Como funciona na prática: no treino, para cada variável e cada classe, o modelo calcula só a **média** e o **desvio padrão** das amostras e desenha uma curva normal com esses dois números. Ele faz isso mesmo que os dados tenham outra forma. Não existe etapa de teste de normalidade.

**KNN (K-Nearest-Neighbors).** Não "aprende" uma fronteira: guarda os dados de treino e, para uma amostra nova, encontra as **K** amostras mais próximas (pela distância euclidiana) e classifica pela classe mais frequente entre elas. K é escolhido por você.

**SVM (Support Vector Machine).** Procura o hiperplano de dimensão (p-1) que serpara as classes em um espaço de p variáveis, escolhendo o que **maximiza a margem**, isto é, o que fica mais longe das amostras mais próximas de cada classe. A classificação de uma amostra nova depende de qual lado do hiperplano ela cai.

**Árvore de decisão.** Constrói uma sequência de testes do tipo "variável $\leq$ limiar?", que dividem os dados em regiões. Cada região corresponde a uma classe, e a amostra nova é classificada seguindo os testes até uma folha. É fácil de interpretar, porque você consegue ler as regras.

**Random Forest.** Conjunto de várias árvores de decisões geradas variando a condição inicial, de modo que não saiam todas iguais. A classe final é decidida por votação entre as árvores.

- Uma árvore única tende a ter **overfitting**, isto é, ela “decora” detalhes e ruídos dos dados de treino. Na floresta, como cada árvore é gerada com **condições iniciais diferentes**, elas erram em amostras diferentes. Na votação, esses erros individuais tendem a se cancelar, e o resultado generaliza melhor que o de qualquer árvore isolada. A Random Forest reduz o overfitting, mas não o elimina.

Vale guardar este contraste: KNN decide **olhando os vizinhos**, Naive-Bayes por **probabilidades**, SVM e árvore por **fronteiras** (o hiperplano de margem máxima e os limiares, respectivamente), e Random Forest combina várias árvores.

### Quando cada modelo se aplica

| Modelo | Ideia em uma linha | Situação típica |
| --- | --- | --- |
| Naive-Bayes | Escolhe a classe mais provável, assumindo variáveis independentes e normais | Base pequena, resposta rápida, variáveis pouco correlacionadas |
| KNN | Vota entre os K vizinhos mais próximos | Poucos dados e poucas variáveis. Fica lento com muitos dados, porque compara com todos na hora de classificar |
| SVM | Hiperplano de margem máxima | Classes razoavelmente separáveis, com muitas variáveis |
| Árvore de decisão | Sequência de testes com limiares | Quando você precisa explicar a decisão |
| Random Forest | Votação entre várias árvores | Quando a árvore única overfita e você aceita perder a interpretabilidade |

## Fronteira vs. vizinhos

A diferença central está em **quando** e **como** o modelo decide:

- **Fronteira (SVM, árvore):** o treino produz uma regra explícita (o hiperplano ou os limiares). Depois, os dados de treino não são mais necessários para classificar.
- **Vizinhos (KNN):** não há regra aprendida. Ele guarda os dados de treino e só decide na hora, comparando a amostra nova com eles.
