# %%
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# %%
data = pd.read_csv("../data/iris.csv")
data.drop(columns="Id", inplace=True)

features = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
target = "Species"

# %%
def add_1s(M):
    return np.column_stack((M, np.ones(M.shape[0])))

# %%
X = data.loc[:, features].to_numpy() # 150 x 4
X = add_1s(X) # 150 x 5

y = LabelEncoder().fit_transform(data[target]) # 150
# setosa -> 0
# versicolor -> 1
# virginica -> 2

# %%
X_train, X_test, y_train, y_test = train_test_split(
	X, y, test_size=0.2, random_state=42, stratify=y
)

Y_onehot_train = np.eye(3)[y_train] # m x 3
Y_onehot_test = np.eye(3)[y_test]

# %%
def ReLU(z):
    return np.maximum(0, z)

def softmax(z):
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

def feedforward(X, W1, W2):
    Z1 = X @ W1 # m x h
    A1 = ReLU(Z1)
    A1 = add_1s(A1) # m x h+1

    Z2 = A1 @ W2 # m x 3
    A2 = softmax(Z2)

    return Z1, A1, Z2, A2

# %%
n_entries = len(features)
n_classes = 3
h_size = 8

# A inicialização de W não pode ser uma matriz de zeros. Com todos os pesos iguais, todos os neurônios ocultos calculam a mesma coisa. Os gradientes também ficam idênticos, então eles recebem a mesma atualização e continuam idênticos sempre. Na prática, a camada oculta funcionaria como um único neurônio.
rng = np.random.default_rng(42)

W1 = rng.normal(0, np.sqrt(2 / n_entries), size=(n_entries + 1, h_size)) # 5 x 8 (He)
W1[-1, :] = 0 # bias começa em zero

W2 = rng.normal(0, np.sqrt(1 / h_size), size=(h_size + 1, n_classes)) # 9 x 3 (Xavier)
W2[-1, :] = 0

# %%
