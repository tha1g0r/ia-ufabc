# Atividade prática

## Derivações

$y = \varphi(s)$. Para derivar $ \partial{y} / \partial{s}$, a $\varphi$ precisa ser derivável. Vou usar a sigmoide, $\varphi(s) = 1 / (1 + e^{-s})$.

**Exemplo com a Iris** (Setosa contra as demias, $\hat{y} = 1$ para Setosa):

- Amostra: uma Setosa com $x_1 = 1.4$ (comprimento da pétala) e $x_2 = 0.2$ (largura da pétala).
- Parâmetros: $w_1 = 0.5$, $w_2 = 0.5$, $b = 0$.
- Erro: $E = (\hat{y} − y)^2$.

Escreva as três derivadas para o peso $w_1$:

> $s = w_1x_1 + w_2x_2 + b = 0.5 \cdot 1.4 + 0.5 \cdot 0.2 + 0 = 0.8$
>
> $y = \dfrac{1}{1 + e^{-s}} = \dfrac{1}{1 + e^{-08}} \approx 0.69$

1. $\partial{s} / \partial{w_1}$
    > $\dfrac{\partial{s}}{\partial{w_1}} = \dfrac{\partial{w_1x_1 + w_2x_2 + b}}{\partial{w_1}} = x_1 = 1.4$

2. $\partial{y} / \partial{s}$
    > $\dfrac{\partial{y}}{\partial{s}} = \dfrac{\partial{\frac{1}{1 + e^{-s}}}}{\partial{s}} = e^{-s} \cdot \dfrac{1}{(1 + e^{-s})^2} = \dfrac{e^{-0.8}}{(1 + e^{-0.8})^2} \approx 0.214$

3. $\partial{E} / \partial{y}$
    > $\dfrac{\partial{E}}{\partial{y}} = \dfrac{\partial{(\hat{y} - y)^2}}{\partial{y}} = -2(\hat{y} - y) = -2(1 - 0.69) = -0.62$

4. $\partial{E} / \partial{w_1}$
    > $\dfrac{\partial{E}}{\partial{w_1}} = \dfrac{\partial{E}}{\partial{y}} \cdot \dfrac{\partial{y}}{\partial{s}} \cdot \dfrac{\partial{s}}{\partial{w_1}} = (-0.62) \cdot 0.214 \cdot 1.4 = -0.186$

## Verificação numérica

A ideia é checar o gradiente sem usar a regra da cadeia. Se $\partial{E} / \partial{w_1}$ é a inclinação de $E$ em função de $w_1$, então para um passo $h$ bem pequeno: $$\dfrac{E(w_1 + h) - E(w_1)}{h} \approx \dfrac{\partial{E}}{\partial{w_1}}$$

1. Calcule $E(w_1)$ com $w_1 = 0.5$, mantendo $w_2 = 0.5$, $b = 0$ e a mesma amostra.
    > $s = w_1x_1 + w_2x_2 + b = \dfrac{1}{2} 1.4 + \dfrac{1}{2} 0.2 + 0 = 0.80$
    >
    > $y = \varphi(s) = \dfrac{1}{1 + e^{-s}} = \dfrac{1}{1 + e^{-0.8}} \approx 0.689974$
    >
    > $E(w_1) = (\hat{y} - y)^2 \approx (1 - 0.689974)^2 \approx 0.096116$

2. Escolha $h = 0.001$ e calcule $E(w_1 + h)$, refazendo $s$, $y$ e $E$ com $w_1 = 0.501$.
    > $E(w_1 + h) = E(0.5 + 0.001) = E(0.501)$
    >
    > $\text{Para } w_1' = 0.501:$
    >
    > $s = w_1x_1 + w_2x_2 + b = 0.501 \cdot 1.4 + \dfrac{1}{2} 0.2 + 0 = 0.80140$
    >
    > $y = \varphi(s) = \dfrac{1}{1 + e^{-s}} = \dfrac{1}{1 + e^{-0.80140}} \approx 0.690274$
    >
    > $E(w_1') = (\hat{y} - y)^2 \approx (1 - 0.690274)^2 \approx 0.095930$

3. Calcule o quociente acima e compare com $-0.186$.
    > $\dfrac{E(w_1') - E(w_1)}{h} \approx \dfrac{0.095930 - 0.096116}{0.001} \approx -0.186$
    >
    > Esse é o $\partial{E} / \partial{w_1}$ calculado anteriormente.

Duas dicas antes de começar:

- Como $E$ muda muito pouco, mantenha pelo menos 6 casas decimais em $y$ e em $E$. Se arredondar para $0.69$, a diferença some e o resultado sai sem sentido.
- Use $y$ sem arredondar, isto é, $\varphi(0.8)$ com todas as casas que sua calculadora der.
