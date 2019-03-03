# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 00:20:09 2019
some k means stuff
@author: Akshay
"""
from __future__ import print_function
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

#from copy import deepcopy
#import csv
import numpy as np
import pandas as pd
#from os import listdir
data = pd.read_csv('data.csv')
print(data.shape)
data.head()
f1 = data['tonnetz'].values
f2 = data['mfcc'].values
X = np.array(list(zip(f1, f2)))

# Standardization
std_data = StandardScaler().fit_transform(X)

plt.scatter(f1, f2, c='black', s=7)



kmeans = KMeans(n_clusters=3)
# Fitting the input data
kmeans = kmeans.fit(X)
# Getting the cluster labels
labels = kmeans.predict(X)
# Centroid values
centroids = kmeans.cluster_centers_


#print acctual list
# Putting ndarray cluster center into pandas DataFrame
coef_df = pd.DataFrame(kmeans.cluster_centers_, columns = ["tonnetz","mfcc"])
# converting ndarray to a nested list 
ndarray2list = kmeans.cluster_centers_.tolist()
print("\nList of clusterd points:\n")
print(ndarray2list)