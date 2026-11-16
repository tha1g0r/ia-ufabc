# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=500,
    n_features=5,
    n_informative=3,
    n_redundant=1,
    n_classes=2,
    class_sep=1.5,
    flip_y=0.02,
    random_state=42
)

# %%
print(f"dimensões de X: {X.shape}") # X é 500x5
print(f"dimensões de y: {y.shape}\n") # y é 500x1

n_feat = X.shape[1] # 5
n_samp = y.shape[0] # 500
print(f"número de features: {n_feat}")
print(f"número de amostras: {n_samp}")

# %%
w = np.zeros(n_feat) # w é 5x1
b = 0.0
learning_rate = 0.001

# %%
def sigmoid(s):
    return 1 / (1 + np.exp(-s))

def feedforward(X, w, b):
    s = X @ w + b
    return sigmoid(s)

def predict(prob):
    return (prob >= 0.5).astype(int)
# %%
for i in range(n_samp):
    amostra = X[i]
    prob = feedforward(amostra, w, b)
    y_pred = predict(prob)
    y_real = y[i]
    print(f"{i + 1}ª amostra: {amostra}")
    print(f"classe predita: {y_pred}")
    print(f"classe real: {y_real}")

    if y_pred == y_real:
        print("sucesso!")
        break
    else:
        print("falha :(\n")
# %%
epochs = 1000
for epoch in epochs:
    pass
