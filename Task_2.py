# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

num_list = list(map(int, input('Введите числа через пробел: ').split()))
print(num_list)
mult_num = 0
for index in range(len(num_list)//2+1):
    mult_num = num_list[index]*num_list[-index-1]
    print(mult_num, end=" ")