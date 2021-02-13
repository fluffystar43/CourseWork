import numpy as np

def dist(A, B, R):
    i = 0
    summa = 0
    while i < R:
        summa += (A[i]-B[i]) ** 2
        i += 1
    r = np.sqrt(summa)
    return r

def class_of_each_point(X, centers):
    m = len(X)
    k = len(centers)    
    distances = np.zeros((m, k))
    for i in range(m):
        for j in range(k):
            distances[i, j] = dist(centers[j], X[i], X.ndim)
    return np.argmin(distances, axis = 1)

def RandomGen(k, X, centers):
    Minimum = min(X[0])
    Maximum = max(X[0])
    Minimum = np.min(X, axis=0)
    Maximum = np.max(X, axis=0)
    i = 0
    while i < len(centers):
        s = 0
        while s < k:
            if int(centers[i][s]) < Minimum[s]:
                centers[i][s] += 0.5
            if int(centers[i][s]) > Maximum[s]:
                centers[i][s] -= 0.5
            if(int(centers[i][s]) < Minimum[s] or int(centers[i][s]) > Maximum[s]):
                s -= 1
            s += 1
        i += 1 

def kmeans(k, X):
    m = int(X.size/X.ndim)
    n = X.ndim
    print("Строк =", m, "\nСтолбцов =", n)
    curr_iteration = prev_iteration = np.zeros(m)
    centers = np.random.random((k, n))
    RandomGen(k, X, centers)
    curr_iteration = class_of_each_point(X, centers)
    while True:
        prev_iteration = curr_iteration
        for i in range(k):
            sub_X = X[curr_iteration == i, :]
            if len(sub_X) > 0:
                centers[i, :] = np.mean(sub_X, axis = 0)
        curr_iteration = class_of_each_point(X, centers)
        if np.all(prev_iteration == curr_iteration):
            print("Центры:")
            return centers