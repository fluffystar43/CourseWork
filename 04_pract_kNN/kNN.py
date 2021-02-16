import numpy as np
import math
from sklearn.preprocessing import normalize

def k_nearest(X, k, obj):
    sub_X = X[:, 0: -1]
    new = np.zeros((17, 2))
    new[:16, :2] = sub_X
    new[16] = obj
    new = normalize(new, axis=0, norm='max')
    for i in range(sub_X.shape[0] - 1):
        sub_X[i] = new[i]
    obj = new[16]
    distance = [dist(i, obj) for i in sub_X]
    sorting = np.argsort(distance)
    sorting = sorting[0:k]
    nearest_classes = X[[sorting], -1]
    unique, counts = np.unique(nearest_classes, return_counts = True)
    object_class = unique[np.argmax(counts)]
    return object_class

def dist(p1, p2):
    return math.sqrt(sum((p1 - p2)**2))