import numpy as np
from tkinter import filedialog as fd




data = np.loadtxt("DataSet.txt")


x = []
y = []

for i in range(len(data)):
    x.append([])
    for j in range(len(data[i])):
        if j == 1:
            y.append(data[i][j])
        else:
            x[i].append(data[i][j])

x = np.array(x)
y = np.array(y)

x_train = x[1::2]
y_train = y[1::2]
x_train = x[1::2]
y_train = y[1::2]

mean = x_train.mean(axis=0) #среднее арифметическое
std = x_train.std(axis=0) #среднеквадратичное (стандартное) отклонение

x_train = (x_train - mean) / std
x = (x - mean) / std

min_y = y_train.min(axis=0) #минимальное значение массива
max_y = y_train.max(axis=0) #максимальное значение массива
y_train = (y_train - min_y) / max_y
y = (y - min_y) / max_y


