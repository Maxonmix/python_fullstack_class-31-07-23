# Задание 5: Обмен цен

# Описание:

# Роман хочет временно поменять цены на самый дорогой и самый дешевый товары.
# Программа должна выводить новый список цен с обмененными значениями.

# Дано:

PRICE_1 = [10, 30, 40, 50]
PRICE_2 = [5, 10, 15, 25, 20]

# Находим индекс максимального и минимального значания в списке

P_1_max = PRICE_1.index(max(PRICE_1))
P_1_min = PRICE_1.index(min(PRICE_1))
P_2_max = PRICE_2.index(max(PRICE_2))
P_2_min = PRICE_2.index(min(PRICE_2))

# Меняем местами максимальное и минимальное значение

PRICE_1[P_1_max], PRICE_1[P_1_min] = PRICE_1[P_1_min], PRICE_1[P_1_max]
PRICE_2[P_2_max], PRICE_2[P_2_min] = PRICE_2[P_2_min], PRICE_2[P_2_max]

# Выводим результат

print(PRICE_1)
print(PRICE_2)