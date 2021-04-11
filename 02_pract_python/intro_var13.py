import math

#Вариант 13
#Задание 1
def massAbs(x, y):
        z = [abs(x[i] - y[i]) for i in range(len(x))]
        return z

X=[1, 2, -3, 4, -5]
Y=[-1, -2, -3, -4, -5]
print("\n", massAbs(X, Y))
    

#Задание 2
def funcWords(list):
    result = ''.join(sorted(sorted(list)))
    return result
    
print("\n", funcWords("PRACTIC_TWO"))


#Задание 3
def euclidean_distance(A, B):
    return math.sqrt(sum([(A[i] - B[i])**2 for i in range(len(A))]))

A = [1.2, 2.4, 3.6]
B = [2.4, 1.1, 5.5]
print("\n", euclidean_distance(A, B))