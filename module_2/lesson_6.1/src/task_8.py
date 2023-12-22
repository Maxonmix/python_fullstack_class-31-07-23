"""Задание 8: Перестановка товаров

Описание:

Роман хочет переставить товары на полке. 
Напишите программу, которая меняет местами два товара
на указанных позициях."""

prod = input("Введите товары: ")
position_1 = int(input("Позиция №1 для ерестановки:  "))
position_2 = int(input("Позиция №2 для ерестановки:  ")) 
prod_list = prod.split(",") 
prod_list[position_1 - 1], prod_list[position_2 - 1] = prod_list[position_2 - 1], prod_list[position_1 - 1]
print(prod)
print(prod_list)
