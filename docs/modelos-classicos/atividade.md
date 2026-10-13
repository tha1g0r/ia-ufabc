# Atividade prática

Para cada situação, diga **qual modelo escolheria** e **uma frase de justificativa**. Algumas podem ter mais de uma resposta defensável, e nesse caso diga qual prefere e por quê.

1. Um banco precisa explicar a um cliente por que o crédito foi negado, apontando regras legíveis, como “renda abaixo de X e dívida acima de Y”.
    > Decision Tree porque tem regras e limiares bem estabelecidos, permitindo interpretação sobre o resultado final.

2. Uma árvore de decisão acerta 100% no treino, mas vai mal no teste. Interpretar a decisão não é exigido.
    > Random Forest porque tente a minimizar o overffiting de uma única Decision Tree a partir de bagging sobre outras trees com condições iniciais diferentes.

3. Você tem poucas flores com 4 medidas cada e quer classificar uma nova comparando-a diretamente com exemp
    > KNN porque usa os dados de treino para calcular distância euclidiana e definir a classe do novo dado com base nos vizinhos mais próximos.

4. As variáveis são aproximadamente normais e pouco correlacionadas, e você quer a classe mais provável com uma resposta rápida.
    > Naive-Bayes porque já assume distribuição normal e não-correlação entre as variáveis. Também utiliza probabilidade mais alta para a classificação final.
