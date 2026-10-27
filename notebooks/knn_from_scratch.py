#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.model_selection import train_test_split
#%%
data = pd.read_csv("../data/breast_cancer_winsconsin.csv")
data.head()
# %%
X = data.drop(columns=["id", "diagnosis", "Unnamed: 32"]).values
y = data["diagnosis"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)
# %%
plt.scatter(X_train[y_train == 'B', 0], X_train[y_train == 'B', 1], color="tab:green", label="Benign")
plt.scatter(X_train[y_train == 'M', 0], X_train[y_train == 'M', 1], color="tab:red", label="Malignant")
plt.xlabel("Compactness Mean")
plt.ylabel("Symmetry Mean")
plt.legend()
plt.show()
# %%
def euclidean_distance(a, b):
    return np.sqrt(np.sum(a - b)**2)
# %%
class KNN:
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, new_points):
        predictions = [self.predict_class(new_point) for new_point in new_points]
        return np.array(predictions)

    def predict_class(self, new_point):
        distances = [euclidean_distance(point, new_point) for point in self.X_train]

        k_nearest_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_nearest_indices]

        most_common = Counter(k_nearest_labels).most_common(1)[0][0]
        return most_common

# %%
knn_5 = KNN(5)
knn_5.fit(X_train, y_train)
predictions = knn_5.predict(X_test)
accuracy = np.mean(predictions == y_test)
print(f"Accuracy: {accuracy:.2f}")
# %%
