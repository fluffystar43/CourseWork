import math

#Вариант 13
#Задание 1
def massAbsDiff(x, y):
    if(type(x) is list and type(y) is list and len(x) == len(y)):
        return [abs(x[i] - y[i]) for i in range(len(x))]
    else:
        raise Exception("x и y - не являются массивами или их размерности не совпадают!")

X=[1, 2, -3, 4, -5]
Y=[-1, -2, -3, -4, -5]
print("\n", massAbsDiff(X, Y))
    
#Задание 2
def characterSort(list):
    return ''.join(sorted(sorted(list)))
    
print("\n", characterSort("PRACTIC_TWO"))

#Задание 3
def euclidean_distance(A, B):
    return math.sqrt(sum([(i - j)**2 for i, j in zip(A, B)]))

A = [1.2, 2.4, 3.6]
B = [2.4, 1.1, 5.5]
print("\n", euclidean_distance(A, B)) 