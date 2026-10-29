# %%
import numpy as np
import pandas as pd
# %%
data = pd.read_csv('../data/mnist/digit-recognizer/train.csv')

data.head()
# %%
data = np.array(data)
m, n = data.shape # m = numero de exemplos | n = numero de pixels em cada exemplo
np.random.shuffle(data)
# %%
data_train = data[0: 1000].T
Y_train = data_train[0]
X_train = data_train[1:n] / 255.0

data_test = data[1000:m].T
Y_test = data_test[0]
X_test = data_test[1:n] / 255.0
# %%
def init_params():
    w1 = np.random.randn(10, 784) * np.sqrt(2 / 784)
    b1 = np.zeros((10, 1))
    w2 = np.random.randn(10, 10) * np.sqrt(2 / 10)
    b2 = np.zeros((10, 1))
    return w1, b1, w2, b2

def relu(Z):
    return np.maximum(0, Z)

def softmax(Z):
    exp_Z = np.exp(Z - np.max(Z, axis=0, keepdims=True))
    return exp_Z / np.sum(exp_Z, axis=0, keepdims=True)

def forward_prop(w1, b1, w2, b2, X):
    Z1 = w1.dot(X) + b1
    A1 = relu(Z1)
    Z2 = w2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

def one_hot(Y, num_classes=10):
    one_hot_Y = np.zeros((num_classes, Y.size))
    one_hot_Y[Y, np.arange(Y.size)] = 1
    return one_hot_Y

def deriv_relu(Z):
    return Z > 0

def back_prop(Z1, A1, Z2, A2, w2, X, Y):
    m = Y.size
    one_hot_Y = one_hot(Y, w2.shape[0])
    dZ2 = A2 - one_hot_Y
    dw2 = 1/m * dZ2.dot(A1.T)
    db2 = 1/m * np.sum(dZ2, axis=1, keepdims=True)
    dZ1 = w2.T.dot(dZ2) * deriv_relu(Z1)
    dw1 = 1/m * dZ1.dot(X.T)
    db1 = 1/m * np.sum(dZ1, axis=1, keepdims=True)
    return dw1, db1, dw2, db2

def update_params(w1, b1, w2, b2, dw1, db1, dw2, db2, alpha):
    w1 = w1 - alpha * dw1
    b1 = b1 - alpha * db1
    w2 = w2 - alpha * dw2
    b2 = b2 - alpha * db2
    return w1, b1, w2, b2

def get_predictions(A2):
    return np.argmax(A2, 0)

def get_accuracy(predictions, Y):
    return np.sum(predictions == Y) / Y.size

def gradient_descent(X, Y, iterations, alpha):
    w1, b1, w2, b2 = init_params()
    for i in range(iterations):
        Z1, A1, Z2, A2 = forward_prop(w1, b1, w2, b2, X)
        dw1, db1, dw2, db2 = back_prop(Z1, A1, Z2, A2, w2, X, Y)
        w1, b1, w2, b2 = update_params(w1, b1, w2, b2, dw1, db1, dw2, db2, alpha)

        if i % 50 == 0:
            print(f"Iteration: {i}\nAccuracy: {get_accuracy(get_predictions(A2), Y)}")

    return w1, b1, w2, b2
# %%
w1, b1, w2, b2 = gradient_descent(X_train, Y_train, 500, 0.1)
# %%
