"""
Задача 2: Сумма подсписка

Описание:

Дан список чисел. Найдите сумму чисел с 2 по 4 элементы включительно.

"""
list = [1, 2, 3, 4, 5]
print(sum(list[1:4]))

# Вариант №2

list_2 = input("Введите список: ")
list_sum = [int(x) for x in list_2.split(",")]
print("Сумма подсписка: ", sum(list_sum[1:4]))