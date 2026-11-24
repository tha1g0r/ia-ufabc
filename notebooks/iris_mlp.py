# %%
import numpy as np
import pandas as pd

# %%
data = pd.read_csv("../data/iris.csv")
data.drop(columns="Id", inplace=True)

# %%
from sklearn.preprocessing import LabelEncoder

X = data.iloc[:, :4].to_numpy() # 150 x 4
X = np.column_stack((X, np.ones(X.shape[0]))) # 150 x 5

y = LabelEncoder().fit_transform(data["Species"]) # 150
# setosa -> 0
# versicolor -> 1
# virginica -> 2

# %%
n_entries = X.shape[1] # 5
h_size = 8
W1 = np.zeros((h_size, n_entries)) # 8 x 5

# %%
