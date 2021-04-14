from PIL import Image
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# Открываем изображение и сохраняем оттенки цветов изображения в 3-мерный массив
im = Image.open('image.jpg')
data = np.array(im.getdata()).reshape([im.height, im.width, 3])

# Создаем матрицу признаков
x = np.arange(0, im.width)
X = np.array([x, x**2.0, x**3.0, x**4.0, x**5.0]).transpose()

# Построение полинома
plt.plot(data[0, :, 0], 'r-')
plt.plot(data[0, :, 1], 'g-')
plt.plot(data[0, :, 2], 'b-')
plt.grid()
plt.show()

# Построение графика с реальными и предсказанными значениями для синего цвета
y = data[0, :, 2]
lm = linear_model.LinearRegression()
lm.fit(X, y)
predicted = lm.predict(X)
plt.plot(y, 'b-')
plt.plot(predicted, 'r-')
plt.grid()
plt.show()

# Вариант 3. Исследовать различные варианты полиномов: второй, третьей, четвёртой, пятой степеней.
# Для каждого из вариантов построить кривую регрессии и отобразить на одном графике вместе с реальными значениями. 
X2 = np.array([x, x**2.0]).transpose()
X3 = np.array([x, x**2.0, x**3.0]).transpose()
X4 = np.array([x, x**2.0, x**3.0, x**4.0]).transpose()

lm.fit(X2, y)
predicted = lm.predict(X2)
plt.plot(y, 'b-')
plt.plot(predicted, 'r-')
plt.grid()
plt.show()

lm.fit(X3, y)
predicted = lm.predict(X3)
plt.plot(y, 'b-')
plt.plot(predicted, 'r-')
plt.grid()
plt.show()

lm.fit(X4, y)
predicted = lm.predict(X4)
plt.plot(y, 'b-')
plt.plot(predicted, 'r-')
plt.grid()
plt.show()

# Вычисление разностей рельных и вычисленных по формуле оттенков
diff = y - predicted
# Кол-во бит для хранения разностей
bits_per_channel = 4
# Рассчитываем кол-во оттенков
threshold = 2**(bits_per_channel-1)-1
# Обрезаем разности, которые выходят за пределы treshold
diff = np.clip(diff, -threshold, threshold)
# Получение усеченных реальных значений оттенков
y = predicted + diff
y = np.clip(np.round(y), 0, 255)

# Получаем измененные значения оттенков всех цветовых каналов для всего изображения
mas = [[0]*3 for i in range(im.height)]
for i in range(im.height):
    for j in range(3):
            y = data[i, :, j]
            lm = linear_model.LinearRegression()
            lm.fit(X, y)
            predicted = lm.predict(X)
            diff = y - predicted
            diff = np.clip(diff, -threshold, threshold)
            y = predicted + diff
            y = np.clip(np.round(y), 0, 255)
            mas[i][j] = y.astype(int)

# Подмена пикселов в исходном изображении
pix = im.load()
for i in range(im.height):
    for j in range(im.width):
        for k in range(3):
            _list = list(pix[j, i])
            _list[k] = mas[i][k][j]
            pix[j, i] = tuple(_list)

# Cохранение изображения
im.save('ready.png')