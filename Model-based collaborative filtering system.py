'''

Recommend items to users based on purchase history
and similarity of ratings provided by other users
who bought items to that of a particular customer.
'''

'''
A model based collaborative filtering technique 
is closen here as it helps in making predictinfg products for a particular user by identifying patterns
based on preferences from multiple user data.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %matplotlib inline
plt.style.use("ggplot")

import sklearn
from sklearn.decomposition import TruncatedSVD
amazon_ratings = pd.read_csv('ratings_Beauty.csv')
amazon_ratings1 = amazon_ratings.head(10000)
print(amazon_ratings1)
ratings_utility_matrix = amazon_ratings1.pivot_table(values='Rating', index='UserId', columns='ProductId', fill_value=0)
print(ratings_utility_matrix.head())


X = ratings_utility_matrix.T
print(X.head())
X1 = X #Unique products in subset of data

#Decomposing the Matrix
SVD = TruncatedSVD(n_components=10)
decomposed_matrix = SVD.fit_transform(X)
print(decomposed_matrix.shape)

#Correlation Matrix
correlation_matrix = np.corrcoef(decomposed_matrix)
print(correlation_matrix.shape)

#Index  of product ID purchased by customer
i = "6117036094"

product_names = list(X.index)
product_ID = product_names.index(i)
print('product_ID',product_ID)

correlation_product_ID = correlation_matrix[product_ID]
print(correlation_product_ID.shape)

Recommend = list(X.index[correlation_product_ID > 0.90])
# Removes the item already bought by the customer
Recommend.remove(i)
print(Recommend[0:9])