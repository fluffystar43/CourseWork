import numpy as np
from kNN import k_nearest
X = np.array([[33., 21., 1],
             [41., 13., 1],
             [18., 22., 1],
             [38., 34., 1],
             [62., 118., 2],
             [59., 137., 2],
             [95., 131., 2],
             [83., 110., 2],
             [185., 155., 3],
             [193., 129., 3],
             [164., 135., 3],
             [205., 131., 3],
             [145., 55., 4],
             [168., 35., 4],
             [135., 47., 4],
             [138., 66., 4]])
height = float(input('Введите рост: '))
weight = float(input('Введите вес: '))
obj = np.array([height, weight])
k = 3
object_class = k_nearest(X, k, obj)
monkeys = {1: 'Лемур', 2: 'Шимпанзe', 3: 'Горилла', 4: 'Орангутан'}
print("\nВид:", monkeys[object_class])
