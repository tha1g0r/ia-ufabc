# Dados e métricas

## Matriz de confusão

As linhas são **Actual** e as colunas são **Predicted**, com *Positive* primeiro:

| | Predicted Positive | Predicted Negative |
| --- | --- | --- |
| **Actual Positive** | TP | FN |
| **Actual Negative** | FP | TN |

## Métricas

- **precision** $= \dfrac{TP}{TP + FP}$. O denominador é a **coluna Predicted Positive**. Pergunta: *"de tudo que eu apontei como positivo, quanto era positivo de verdade?"*

- **recall** $= \dfrac{TP}{TP + FN}$. O denominador é a **linha Actual Positive**. Pergunta: *"de todos os positivos que existiam, quantos eu encontrei?"*

- **accuracy** $= \dfrac{TP + TN}{TP + TN + FP + FN}$. É a diagonal dividida pelo total.

### Exemplo

Do **exemplo da fraude**, com as fórmulas. São 100 amostras, 1 fraude, e o modelo diz *"não-fraude"* sempre. Então, a matriz de confusão:

| | Predicted Positive | Predicted Negative |
| --- | --- | --- |
| **Actual Positive** | $TP = 0$ | $FN = 1$ |
| **Actual Negative** | $FP = 0$ | $TN = 99$ |

- $\text{accuracy} = \dfrac{0 + 99}{0 + 99 + 0 + 1} = \dfrac{99}{100} = 0.99$

    A accuracy é $99\%$.

- $\text{recall} = \dfrac{0}{0 + 1} = \dfrac{0}{1} = 0$

    O recall é $0\%$.

- $\text{precision} = \dfrac{0}{0 + 0} = \dfrac{0}{0} = \textit{undefined}$

    A precision é $0/0$, indefinida, porque o modelo nunca apontou nada.

A accuracy esconde essa falha, e o recall a revela de imediato.

Sobre o trade-off: na prática, subir uma das duas métricas costuma custar a outra. Por isso temos o **F1**, que combina as duas.

### Métricas por classe

**Contexto:**
> TP, FN, FP e TN são conceitos **binários**, de “positivo” contra “negativo”. Para usá-los na Iris, por exemplo, você escolhe uma classe e a trata como **positivo**. Todas as outras viram **negativo**. Com Versicolor como positivo, a matriz 3×3 passa a ser vista como uma matriz 2×2 da pergunta *“é Versicolor ou não é?”*.
>
> Para cada célula da sua tabela, responda a duas perguntas:
>
> 1. O que era de verdade (a linha) é **Versicolor** ou **não-Versicolor**?
> 2. O que o modelo disse (a coluna) foi **Versicolor** ou **não-Versicolor**?
>
> Combinando as duas respostas, você classifica a célula:
>
> - Era Versicolor e o modelo disse Versicolor → **TP**
> - Era Versicolor e o modelo disse outra coisa → **FN**
> - Não era Versicolor e o modelo disse Versicolor → **FP**
> - Não era Versicolor e o modelo disse outra coisa → **TN**

Útil por três motivos:

1. **A acurácia global esconde onde o modelo erra**. É a mesma falha do exemplo da fraude, só que com várias classes. Um número único mistura todas as classes. Um modelo pode acertar tudo em duas classes e ir mal na terceira, e o número global ainda parece bom. Quando você olha uma classe por vez, vê qual delas está falhando.
2. **O custo do erro costuma ser diferente por classe**. Em muitos problemas reais existe uma classe de interesse (fraude, doença) e o resto. Nesses casos, “classe de interesse contra o resto” é a pergunta que importa, e precision e recall dessa classe respondem a ela diretamente.
3. **Mostra onde melhorar**. Na matriz da atividade, a Setosa é separada sem nenhum erro. Os erros aparecem só entre as outras duas classes. A visão por classe mostra isso e indica onde ajustar o modelo ou as características usadas.
