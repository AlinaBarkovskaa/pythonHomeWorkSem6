# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#  (т.е. не меньше заданного минимума и не больше заданного максимума)

number = int(input('Введите number: ')) 
list_array = [int(input('Введите n: ')) for _ in range(number)]
rezult = []
max = int(input('Введите максимальный элемент: '))
min = int(input('Введите минимальный элемент: '))
for i in range(len(list_array)):
    if list_array[i] >= min and list_array[i] <= max:
        rezult.append(list_array[i])
print(rezult)       