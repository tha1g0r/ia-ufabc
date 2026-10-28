# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
plt.rcParams['figure.figsize'] = (10, 8)
# %%
# # Gerando o Dataset

def get_linear_curve(x, w, b=0, noise_scale=0):
    return w * x + b + noise_scale * np.random.randn(x.shape[0])

x = np.arange(-20, 30.1, 0.5)
Y = get_linear_curve(x, 1.8, 32, noise_scale=2.5) # inclinação da reta e bias real da conversão Celsius -> Fahrenheit
# %%
plt.scatter(x, Y)
plt.xlabel("°C", fontsize=15)
plt.ylabel("°F", fontsize=15)
# %%
# # Modelo
#
# 1. Inicializar os pesos e bias
# 2. Feedforward
# 3. Calcular a perda
# 4. Backpropagation
# %%
# Inicialização
w = np.random.rand(1)
b = np.zeros(1)

# Feedforward
def forward(inputs, weight, bias):
    return weight * inputs + bias

# Perda
def mse(targets, outputs):
    return (targets - outputs) ** 2

# Backpropagation
def backpropagation(inputs, outputs, targets, w, b, learn_rate):
    error = targets - outputs

    dw = learn_rate * np.mean((-2) * inputs * error)
    w -= dw

    db = learn_rate * np.mean((-2) * error)
    b -= db

    return w, b
# %%
# fit
def model_fit(x, Y, w, b, epochs=200, learn_rate=0.001):
    for epoch in range(epochs):
        y = forward(x, w, b)
        loss = np.mean(mse(Y, y))
        w, b = backpropagation(x, y, Y, w, b, learn_rate)

        if (epoch + 1) % 50 == 0:
            print(f"Epoch: {epoch + 1}/{epochs} | Loss: {loss:.4f}")

    return w, b
# %%
x = np.arange(-10, 10.1, 0.5)
Y = get_linear_curve(x, 1.8, 32, noise_scale=2)
w = np.random.rand(1)
b = np.zeros(1)

w, b = model_fit(x, Y, w, b, epochs=1000, learn_rate=0.002)
print(f"w = {w[0]:.3f}, b = {b[0]:.3f}")
# %%
plt.scatter(x, Y)
plt.plot(x, get_linear_curve(x, w, b), 'r')
# %%
