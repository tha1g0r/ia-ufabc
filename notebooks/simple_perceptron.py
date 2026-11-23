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

def get_loss(X, w, y):
    eps = 1e-15
    probs = np.clip(feedforward(X, w), eps, 1 - eps)
    losses = -(y * np.log(probs) + (1 - y) * np.log(1 - probs))
    return np.mean(losses)

# %%
w = np.zeros(n_feat) # w é n_feats x 1
print(f"w inicial: {w}\n")

print("treinando...")
learning_rate = 0.001

train_acc_history, val_acc_history = [], []
ideal_acc_w, ideal_val_acc_value, ideal_val_acc_epoch = w.copy(), -np.inf, None

train_loss_history, val_loss_history = [], []
ideal_loss_w, ideal_val_loss_value, ideal_val_loss_epoch = w.copy(), np.inf, None

epochs = 3000
for epoch in range(epochs):
    # sample shuffle per each epoch
    idxs = np.random.permutation(len(X_train))
    X_train = X_train[idxs]
    y_train = y_train[idxs]

    # train per each sample
    for i_samp in range(len(X_train)):
        x = X_train[i_samp]
        y_pred = feedforward(x, w)
        y_real = y_train[i_samp]
        error = y_pred - y_real
        w -= learning_rate * error * x

    # accuracies per each epoch
    # train accuracy
    partial_train_acc = get_accuracy(X_train, w, y_train)
    train_acc_history.append(partial_train_acc)
    # validation accuracy
    partial_val_acc = get_accuracy(X_val, w, y_val)
    if not val_acc_history or partial_val_acc >= max(val_acc_history):
        ideal_acc_w, ideal_val_acc_value, ideal_val_acc_epoch = w.copy(), partial_val_acc, epoch + 1
    val_acc_history.append(partial_val_acc)

    # losses per each epoch
    # train loss
    partial_train_loss = get_loss(X_train, w, y_train)
    train_loss_history.append(partial_train_loss)
    # validation loss
    partial_val_loss = get_loss(X_val, w, y_val)
    if not val_loss_history or partial_val_loss <= min(val_loss_history):
        ideal_loss_w, ideal_val_loss_value, ideal_val_loss_epoch = w.copy(), partial_val_loss, epoch + 1
    val_loss_history.append(partial_val_loss)

    # print per each 200 epochs
    if (epoch + 1) % 200 == 0:
        print(f"{epoch + 1}ª época | acurácia de validação: {partial_val_acc:.4f} | perda de validação: {partial_val_loss:.4f}")

acc_f = get_accuracy(X_train, w, y_train)
print(f"\nacurácia final de treino: {acc_f:.4f}")
print(f"w final de treino: {w}\n")

# %%

print(f"acurácia máxima de validação: {ideal_val_acc_value:.4f} | época: {ideal_val_acc_epoch}")
print(f"w ideal de validação (acurácia): {ideal_acc_w}")

print(f"\nperda mínima de validação: {ideal_val_loss_value:.4f} | época: {ideal_val_loss_epoch}")
print(f"w ideal de validação (perda): {ideal_loss_w}")

# %%
epocas = range(1, len(train_acc_history) + 1)
plt.figure(figsize=(8, 5))
plt.plot(epocas, train_acc_history, label="Train")
plt.plot(epocas, val_acc_history, label="Val")
plt.xlabel("Época")
plt.ylabel("Acurácia")
plt.title("Progressão da acurácia por época")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(8, 5))
plt.plot(epocas, train_loss_history, label="Train")
plt.plot(epocas, val_loss_history, label="Val")
plt.xlabel("Época")
plt.ylabel("Loss")
plt.title("Progressão da loss por época")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# %%
print("aplicando w ideal aos dados de teste...\n")

print("considerando o w ideal da acurácia:")
acc_test_val = get_accuracy(X_test, ideal_acc_w, y_test)
print(f"acurácia de teste: {acc_test_val:.4f}")
loss_test_val = get_loss(X_test, ideal_acc_w, y_test)
print(f"perda de teste: {loss_test_val:.4f}")

print("\nconsiderando o w ideal da perda:")
acc_test_val = get_accuracy(X_test, ideal_loss_w, y_test)
print(f"acurácia de teste: {acc_test_val:.4f}")
loss_test_val = get_loss(X_test, ideal_loss_w, y_test)
print(f"perda de teste: {loss_test_val:.4f}")

# %%
