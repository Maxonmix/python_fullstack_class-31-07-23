# Задание 2: Поиск вдохновения

# Описание:

# Роман хочет добавить слоган для своего магазина и подумывает о слове
# "Creative". Но в начале он хочет проверить есть ли такое слово в описаниях
# на сайте. Найдите индекс первого вхождения этого слова в различных описаниях
# магазина. Если такого слова нет нужно вернуть -1.

# Константы из задания:

TEXT_1 = "Welcome to the Creative Space"
TEXT_2 = "We don`t have realitive in here."
TEXT_3 = "Creative ideas for you"
TXT_CREATIVE = "Creative"

# Ответ на задание:

print(TEXT_1.find(TXT_CREATIVE))
print(TEXT_2.find(TXT_CREATIVE))
print(TEXT_3.find(TXT_CREATIVE))


