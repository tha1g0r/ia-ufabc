# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=1000,
    n_features=5,
    n_informative=3,
    n_redundant=1,
    n_classes=2,
    class_sep=1.5,
    flip_y=0.02,
    random_state=42
)

X = np.column_stack((X, np.ones(X.shape[0])))

# %%
print(f"dimensões de X: {X.shape}") # X é n_samps x n_feats
print(f"dimensões de y: {y.shape}\n") # y é n_samps x 1

n_feat = X.shape[1] # 6
n_samp = y.shape[0] # 1000
print(f"número de features: {n_feat}")
print(f"número de amostras: {n_samp}")

# %%
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=300,
    stratify=y,
    random_state=42
)

X_train, X_val, y_train, y_val = train_test_split(
    X_train,
    y_train,
    test_size=200,
    stratify=y_train,
    random_state=42
)

# %%
def sigmoid(s):
    return 1 / (1 + np.exp(-s))

def feedforward(X, w):
    s = X @ w
    return sigmoid(s)

def get_class(prob):
    return (prob >= 0.5).astype(int)

def get_accuracy(X, w, y):
    probs = feedforward(X, w)
    predicted_classes = get_class(probs)
    return np.mean(predicted_classes == y)

# %%
w = np.zeros(n_feat) # w é n_feats x 1
print(f"w inicial: {w}\n")

print("treinando...")
learning_rate = 0.001

acc_train_history, acc_val_history = [], []
w_train_ideal, w_val_ideal = w.copy(), w.copy()

epochs = 1000
for epoch in range(epochs):
    for i_samp in range(len(X_train)):
        x = X_train[i_samp]
        y_pred = feedforward(x, w)
        y_real = y_train[i_samp]
        error = y_pred - y_real
        w -= learning_rate * error * x

    # train accuracy
    acc_train_p = get_accuracy(X_train, w, y_train)
    if not acc_train_history or acc_train_p > max(acc_train_history):
        w_train_ideal = w.copy()
    acc_train_history.append(acc_train_p)

    # validation accuracy
    acc_val_p = get_accuracy(X_val, w, y_val)
    if not acc_val_history or acc_val_p > max(acc_val_history):
        w_val_ideal = w.copy()
    acc_val_history.append(acc_val_p)

    if (epoch + 1) % 100 == 0:
        print(f"{epoch + 1}ª época | acurácia de treino: {acc_train_p:.4f} | acurácia de validação: {acc_val_p:.4f}")

# %%
acc_f = get_accuracy(X_train, w, y_train)
print(f"acurácia de treino final: {acc_f:.4f}")
print(f"w final: {w}\n")

acc_train_max = max(acc_train_history)
epoca_train_max = acc_train_history.index(acc_train_max) + 1
print(f"acurácia de treino máxima: {acc_train_max:.4f} | época: {epoca_train_max}")
print(f"w ideal de treino: {w_train_ideal}\n")

acc_val_max = max(acc_val_history)
epoca_val_max = acc_val_history.index(acc_val_max) + 1
print(f"acurácia de validação máxima: {acc_val_max:.4f} | época: {epoca_val_max}")
print(f"w ideal de validação: {w_val_ideal}")

# %%
epocas = range(1, len(acc_train_history) + 1)
plt.figure(figsize=(8, 5))
plt.plot(epocas, acc_train_history, label="Train")
plt.plot(epocas, acc_val_history, label="Val")
plt.xlabel("Época")
plt.ylabel("Acurácia")
plt.title("Progressão da acurácia por época")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# %%
print("aplicando w ideal aos dados de teste...\n")

acc_test_train = get_accuracy(X_test, w_train_ideal, y_test)
print(f"acurácia de teste (w ideal de treino): {acc_test_train:.4f}")

acc_test_val = get_accuracy(X_test, w_val_ideal, y_test)
print(f"acurácia de teste (w ideal da validação): {acc_test_val:.4f}")

# %%
