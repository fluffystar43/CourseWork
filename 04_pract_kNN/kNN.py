import numpy as np
import math
from sklearn.preprocessing import StandardScaler

def k_nearest(X, k, obj):
    scaler = StandardScaler()
    sub_X = X[:, 0: -1]
    scaler.fit(sub_X)
    average = scaler.mean_
    standard_deviation = np.std(sub_X, axis = 0)
    for i in range(len(obj)):
        obj[i] = (obj[i]-(np.mean(sub_X, axis=0))[i])/(np.std(sub_X, axis=0))[i]
    for i in range(sub_X.shape[1]):
        sub_X[:, i] = (sub_X[:, i] - average[i])/standard_deviation[i]
    distance = [euclidean_distance(i, obj) for i in sub_X]
    sorting = np.argsort(distance)
    sortingMas = sorting[0:k]
    nearest_classes = X[[sortingMas], -1]
    unique, counts = np.unique(nearest_classes, return_counts = True)
    object_class = unique[np.argmax(counts)]
    return object_class

def euclidean_distance(p1, p2):
    return math.sqrt(sum((p1 - p2)**2))