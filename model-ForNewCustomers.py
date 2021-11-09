import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Recommendation System - Part I
'''
Product pupularity based system targetted 
at new customers
'''
plt.style.use("ggplot")

amazon_ratings = pd.read_csv('ratings_Beauty.csv')
amazon_ratings = amazon_ratings.dropna()
print(amazon_ratings.head())
print(amazon_ratings.shape)
popular_products = pd.DataFrame(amazon_ratings.groupby('ProductId')['Rating'].count())
most_popular = popular_products.sort_values('Rating', ascending=False)


#most_popular.head(30).plot(kind = "bar")
#plt.bar(most_popular.head(30))
most_popular.head(30).plot(kind = "bar")
plt.show()