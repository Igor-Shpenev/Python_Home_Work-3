# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число: '))
dv_num = 0
my_list = []
while num > 0:
    dv_num = num % 2
    num //= 2
    my_list.append(dv_num)
my_list = my_list[::-1]

for number in my_list:
    print(number, end='')
