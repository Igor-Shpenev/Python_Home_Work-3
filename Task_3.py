# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
n = int(input('Введите кол-во элементов списка: '))
float_list = []
for _ in range(n):                                                      
    float_list.append(round(random.uniform(1, 10), 2))
print(float_list)

int_list = []
for num in float_list:
    num *= 100                                                           
    int_list.append(int(num) % 100)
print(int_list)

result = (max(int_list) - min(int_list)) / 100
print(result)
