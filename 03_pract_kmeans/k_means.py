import numpy as np


def euclidean_distance(A, B):
    return np.sqrt(np.sum(np.power(A-B, 2)))

def class_of_each_point(X, centers):
    m = len(X)
    k = len(centers)    
    distances = np.zeros((m, k))
    for i in range(m):
        for j in range(k):
            distances[i, j] = euclidean_distance(centers[j], X[i])
    return np.argmin(distances, axis = 1)

def kmeans(k, X):
    m = X.shape[0]
    n = X.shape[1]
    print("Строк =", m, "\nСтолбцов =", n)
    curr_iteration = prev_iteration = np.zeros(m)
    Min = np.min(X, axis=0)
    Max = np.max(X, axis=0)
    centers = np.random.randint(Min, Max, size=[k, n]).astype('float')    
    curr_iteration = class_of_each_point(X, centers)
    while np.any(curr_iteration != prev_iteration):
        prev_iteration = curr_iteration
        for i in range(k):
            sub_X = X[curr_iteration == i, :]
            if len(sub_X) > 0:
                centers[i, :] = np.mean(sub_X, axis = 0)
        curr_iteration = class_of_each_point(X, centers)
        if np.all(prev_iteration == curr_iteration):
            return centers