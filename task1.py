# Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
first_elem = int(input('Введите первый элемент массива: '))
count = int(input('Введите кол-во элементов: '))
difference = int(input('Введите разность между элеметами: '))
for i in range (count):
    print(first_elem + i * difference)
