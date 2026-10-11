# Atividade prática

A base Iris tem 150 amostras, 50 de cada classe. Suponha que um classificador (por exemplo, o Naive-Bayes) produziu esta matriz de confusão no conjunto inteiro. Os valores são hipotéticos, escolhidos para o exercício.

| | Predicted Setosa | Predicted Versicolor | Predicted Virginica |
| --- | --- | --- | --- |
| **Actual Setosa** | 50 | 0 | 0 |
| **Actual Versicolor** | 0 | 45 | 5 |
| **Actual Virginica** | 0 | 2 | 48 |

**Tarefas:**

1. Calcule a **accuracy** global.
    > $$
    > \text{accuracy} = \dfrac{50 + 45 + 48}{150} = \dfrac{143}{150} = 0.9533 = 95.33\%
    > $$

2. Tratando **Versicolor como positivo**, dê os valores de **TP, FN, FP e TN**. Confira se a soma dá 150.
    > Tratando Versicolor como positivo:
    >
    > | | |
    > | --- | --- |
    > | $TP =  45$ | $FN  = 5$ |
    > | $FP = 2$ | $TN = 50 + 48 = 98$ |
    >
    > Da nossa tabela, $45 + 5 + 2 + 98 = 150$.

3. Calcule a **precision** e o **recall** de Versicolor. Depois escreva, em uma frase cada, o que esses dois números significam neste problema, sem usar a fórmula.
    > $\text{precision} = \dfrac{TP}{TP + FP} = \dfrac{45}{47} = 0.9574 = 95.74\%$
    >
    > Isso significa que, de todos os positivos que o modelo previu, ele acertou em $95.74\%$. Ou seja, das amostras que o modelo chamou de Versicolor, $95,74\%$ eram de fato Versicolor.
    >
    > $\text{recall} = \dfrac{TP}{TP + FN} = \dfrac{45}{50} = 0.90 = 90\%$
    >
    > Isso significa que, de todos os positivos que existiam, o modelo acertou capturou $90\%$ deles. Ou seja, das 50 Versicolor reais, o modelo encontrou $90\%$.

4. Faça o mesmo para **Virginica** (precision e recall). Qual das duas classes, Versicolor ou Virginica, tem o pior recall? E o pior precision?
    > Tratando Virginica como positivo:
    >
    > | | |
    > | --- | --- |
    > | $TP = 48$ | $FN = 2$ |
    > | $FP = 5$ | $TN = 50 + 45 = 95$ |
    >
    > Da tabela, $48 + 2 + 5 + 95 = 150$.
    >
    > $\text{precision} = \dfrac{TP}{TP + FP} = \dfrac{48}{53} = 0.9057 = 90.57\%$
    >
    > Isso significa que, das amostras que o modelo predisse Virginica, $90.57\%$ realmente eram Virginica.
    >
    > $\text{recall} = \dfrac{TP}{TP + FN} = \dfrac{48}{50} = 0.96 = 96\%$
    >
    > Isso significa que, de todas as 50 Virginicas reais, o modelo encontrou $96\%$ delas.
    >
    > ---
    >
    > Virginica tem a pior precision e Versicolor tem o pior recall. Isso mostra que o modelo é mais seguro ao classificar um Versicolor, mas falha mais em capturar todas as flores dessa espécie. Por outro lado, o modelo é bom em capturar grande parte das Virginicas, mas pode acabar classificando uma outra espécie como Virginica por engano.

5. Calcule o **F1** e a **especificidade** da classe Versicolor.
    > $\text{F1}_\text{ve} = 2 \times \dfrac{\text{precision}_\text{ve} \times \text{recall}_\text{ve}}{\text{precision}_\text{ve} + \text{recall}_\text{ve}} = 2 \times \dfrac{0.9574 \times 0.90}{0.9574 + 0.90} = 0.9278 = 92.78\%$
    >
    > Como a especificidade calcula **quanto dos casos realmente negativos** o modelo reconheceu corretamente, seu denominador será os casos realmente negativos, ou seja, $FP + TN$ e seu numerador, $TN$:
    >
    > $\text{especificidade} = \dfrac{TN}{FP + TN} = \dfrac{98}{100} = 0.98 = 98\%$
    >
    > Ou seja, das amostras que não eram Versicolor, o modelo reconheceu corretamente $98\%$ delas.

6. Separe **TP, FN, FP e TN** da classe **Setosa**. Calcule sua **precision** e o **recall** e escreva em uma frase o que esses valores indicam sobre o modelo para essa classe.
    > Tratando Setosa como positivo:
    >
    > | | |
    > | --- | --- |
    > | $TP = 50$ | $FN = 0$ |
    > | $FP = 0$ | $TN = 45 + 5 + 2 + 48 = 100$ |
    >
    > Da tabela, $50 + 0 + 0 + 100 = 150$.
    >
    > $\text{precision} = \dfrac{TP}{TP + FP} = \dfrac{50}{50} = 1 = 100\%$
    >
    > Ou seja, de todas as amostras que o modelo marcou como Setosa, $100\%$ delas eram realmente setosas.
    >
    > $\text{recall} = \dfrac{TP}{TP + FN} = \dfrac{50}{50} = 1 = 100\%$
    >
    > Ou seja, de todas as amostras que realmente eram Setosa, o modelo capturou $100\%$ delas.
    >
    > **Conclusão:** O modelo separa Setosa **perfeitamente** das outras classes. Acertou em todas as vezes que predisse Setosa e não deixou nenhuma amostra dessa espécie passar.
