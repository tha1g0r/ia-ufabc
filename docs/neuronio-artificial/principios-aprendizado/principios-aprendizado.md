# Princípios de Aprendizado

Para treinar um neurônio ou uma rede neural, precisamos fornecer para uma rede uma informação do quão correta ou errada é a sua previsão. Para isso, precisamos de dados rotulados (*aprendizado supervisionado*).

Vamos analisar a proposta de Rosenblatt em um problema de classificação: o uso de uma função desenvolvida por Donald Hebb (Aprendizado Hebbiano).

## Aprendizado Hebbiano

Baseia-se na ideia de que **conexões entre neurônios se fortalecem quando eles são ativados simultâneamente**.

A regra de Hebb pode ser resumida em: *"Neurônios que disparam juntos, conectam-se mais fortemente."*

### Como funciona?

- Cada conexão entre neurônios possui um peso, que determina a influência de um neurônio sobre outro.
- Quando um neurônio de entrada e um neurônio de saída são ativados juntos, o peso da conexão aumenta.
- A rede aprende identificando associações entre padrões de ativação, sem precisar de um professor que indique a resposta correta.

A forma matemática é: $$\Delta w_{ij} = \eta (y_j - \hat{y}_j) \cdot x_i$$

Em que:

- $\Delta w_{ij}$: quanto o peso da conexão será alterado.
- $\eta$: taxa de aprendizado que controla o tamanho da alteração.
- $y_j$: valor desejado (correto) para a saída $j$.
- $\hat{y}_j$: valor que a rede efetivamente produziu.
- $x_i$: valor recebido pelo neurônio de entrada $i$.

#### Como a fórmula funciona?

O termo $y_j - \hat{y}_j$ representa o erro da saída:

- Se a rede produziu um valor menor que o desejado, o erro é positivo.
- Se produziu um valor maior que o desejado, o erro é negativo.
- Se acertou exatamente, o erro é zero e, nessa regra, o peso não é alterado.

Esse erro é multiplicado pela entrada $x_i$ e pela taxa de aprendizado $\eta$. Assim, o peso é ajustado de acordo com o erro e com a contribuição daquela entrada.

**Por que $x_i$ multiplica?** Cada entrada contribui para a saída na proporção do seu valor. Uma entrada grande influenciou mais o erro e recebe um ajuste maior. Uma entrada com $x_i = 0$ não influenciou nada, então seu peso não muda.

**E $\eta$?** Intuitivamente, é o tamanho do passo. Um $\eta$ pequeno corrige devagar, com cautela, e um $\eta$ grande corrige em saltos maiores.

### Regra hebbiana original

Hebb fortalece a conexão quando entrada e saída ficam ativas juntas, sem comparar com nenhum rótulo. A regra da aula acrescenta o termo de erro ($y_j − \hat{y}_j$), então só altera os pesos quando há erro, e o sinal depende do tipo de erro.

## Regra do bias

Em $u_j = \sum_{i} w_{ij} \cdot x_i + b_j$, $b_j$ é um peso $w_{0j}$ cuja entrada $x_0 = 1$. Assumindo $i = 0$, $\Delta w_{0j} = \eta (y_j - \hat{y}_j) \cdot x_0 \rightarrow \Delta b_j = \eta (y_j - \hat{y}_j)$.
