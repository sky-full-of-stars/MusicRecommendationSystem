# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 00:20:09 2019
some k means stuff
@author: Akshay
"""
from __future__ import print_function
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#from copy import deepcopy
#import csv
import numpy as np
import pandas as pd
import csv
#from os import listdir
data = pd.read_csv('data.csv')
def k_means():
    f1 = data['tonnetz'].values
    f2 = data['mfcc'].values
    f3 = data['chroma'].values
    f4 = data['mel'].values
    f5 = data['contrast'].values
    X = np.array(list(zip(f1, f2, f3, f4, f5)))
    
    # Standardization
    X = StandardScaler().fit_transform(X)
    
    #plot
    plt.scatter(f1, f2, c='black', s=7)
    
    #Find the optimal number of clusters 
    Sum_of_squared_distances = []
    K = range(1,15)
    for k in K:
        km = KMeans(n_clusters=k)
        km = km.fit(X)
        Sum_of_squared_distances.append(km.inertia_)
    
    
    #decide the number of clusters using the plot.Going with 7 in this case.
    plt.plot(K, Sum_of_squared_distances, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
    plt.show()
    
    #after analyzing the plot, determine the number of clusters
    n_clusters = 7
    
    kmeans = KMeans(n_clusters=n_clusters)
    # Fitting the input data
    kmeans.fit(X)
    # Getting the cluster labels
    labels = kmeans.predict(X)
    # Centroid values
    centroids = kmeans.cluster_centers_
    #print acctual list
    # Putting ndarray cluster center into pandas DataFrame
    #coef_df = pd.DataFrame(kmeans.cluster_centers_, columns = ["tonnetz","mfcc","chroma","mel","constrast"])
    # converting ndarray to a nested list 
    #ndarray2list = kmeans.cluster_centers_.tolist()
    return centroids,labels,n_clusters

def store_in_file(centroids,labels,n_clusters):
    #creating a file for each cluster and setting the header
    for i in range(0,n_clusters):
        filename = 'cluster'+str(i)+'.csv'
        header =  'filename tonnetz mfcc chroma mel contrast'
        header = header.split()
        file = open(filename, 'w', newline='')
        with file:
            writer = csv.writer(file)
            writer.writerow(header)
    
    #seggregating songs into clusters
    for i in range(0,500):
        filename = 'cluster'+str(labels[i])+'.csv'
        to_append = f'{data.iloc[i,0]} {data.iloc[i,1]} {data.iloc[i,2]} {data.iloc[i,3]} {data.iloc[i,4]} {data.iloc[i,5]} '
        file = open(filename, 'a', newline='')
        with file:
            writer = csv.writer(file)
            writer.writerow(to_append.split())
    
    #store the centroid points in a file
    filename = 'centroid.csv'
    header =  'cluster_number tonnetz mfcc chroma mel contrast'
    header = header.split()
    file = open(filename, 'w', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(header)
    
    for i in range(n_clusters):
        file = open(filename, 'a', newline='')
        to_append = f'{i} {centroids[i][0]} {centroids[i][1]} {centroids[i][2]} {centroids[i][3]} {centroids[i][4]}'
        with file:
            writer = csv.writer(file)
            writer.writerow(to_append.split())
        
            
centroids,labels,n_clusters = k_means()
store_in_file(centroids,labels,n_clusters)

