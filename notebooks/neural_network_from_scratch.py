# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %%
data = pd.read_csv('../data/mnist/digit-recognizer/train.csv')

data.head()
# %%
data = np.array(data)
m, n = data.shape # m = numero de exemplos | n = numero de pixels em cada exemplo
np.random.shuffle(data)
# %%
data_train = data[0: 1000].T
T_train = data_train[0]
X_train = data_train[1:n]

data_test = data[1000:m].T
Y_test = data_test[0]
X_test = data_test[1:n]
# %%
def init_params():
    w1 = np.random.randn(10, 784)
    b1 = np.randon.randn(10, 1)
    w2 = np.random.randn(10, 784)
    b2 = np.randon.randn(10, 1)
    return w1, b1, w2, b2

def ReLU(Z):
    np.maximum(0, Z)

def softmax(Z):
    return np.exp(Z) / np.sum(np.exp(Z))

def forward_prop(w1, b1, w2, b2, X):
    Z1 = w1 @ X + b1
    A1 = ReLU(Z1)
    Z2 = w2 @ A1 + b2
    A2 = softmax(A1)
    return Z1, A1, Z2, A2

def back_prop(Z1, A1, Z2, A2, Y):
    pass