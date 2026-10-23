import matplotlib.pyplot as plt  # подключаем графики
import numpy  # подключаем numpy

# создаем иксы от 0.1 до 5 с шагом 0.05
x = numpy.arange(0.1, 5, 0.05)

# считаем x^2
a = x * x

# считаем e^x
b = numpy.exp(x)

# считаем ln(x)
c = numpy.log(x)

# считаем x^3
d = x * x * x

# целые иксы для точек
i = numpy.array([1, 2, 3, 4, 5])

# создаем окно
plt.figure()

# рисуем x^2 красным (линия без маркеров)
plt.plot(x, a, color='red', label='x^2')
# ставим точки кружками только на целых иксах
plt.plot(i, i * i, 'ro', color='red')

# рисуем e^x синим (линия без маркеров)
plt.plot(x, b, color='blue', label='e^x')
# ставим точки крестиками только на целых иксах
plt.plot(i, numpy.exp(i), 'bx', color='blue')

# рисуем ln(x) зеленым (линия без маркеров)
plt.plot(x, c, color='green', label='ln(x)')
# ставим точки треугольниками только на целых иксах
plt.plot(i, numpy.log(i), 'g^', color='green')

# рисуем x^3 фиолетовым (линия без маркеров)
plt.plot(x, d, color='purple', label='x^3')
# ставим точки звездочками только на целых иксах
plt.plot(i, i * i * i, 'm*', color='purple')

# показываем где какая функция
plt.legend()

# включаем сетку
plt.grid()

# пишем заголовок
plt.title("Графики функций")

# выводим график
plt.show()