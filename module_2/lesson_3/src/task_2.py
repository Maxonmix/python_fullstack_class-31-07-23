# Задача 2: Кто на смене?

# Описание:

# Роман нанял продавцов в свой магазин, но теперь их слишком много и не понятно кто работает в какие дни. Он посчитал, что в чётные дни будет работать Света и Олег, а в нечётные Маша и Паша. Теперь он просит написать программу для информационного табло, где будет выводиться график работы. Роман понимает, что скоро уволит кого-то из сотрудников, поэтому просит сохранить их имена в переменные.

# Реализуйте программу, которая выводит график работы сотрудников в 3 строки. 2 строка должна быть пустой. Вывод оформите используя передачу нескольких аргументов в функцию print. Каждое имя нужно сохранить в отдельную переменную.\

# Вариант №1: Без запроса имен

NAME_1 = "Света"
NAME_2 = "Олег"
NAME_3 = "Маша"
NAME_4 = "Паша"

#print("В четные дни работают: " + NAME_1 + " " + NAME_2)
#print()
#print("В нечетные дни работают: " + NAME_3 + " " + NAME_4)

# Вариант №2: С запросом имен

#even = input("Имена сотрудников работающих по четным дням: ")
#not_even = input("Имена сотрудников работающих в не четные дни: ")
#print("В четные дни работают: " + even)
#print()
#print("В не четные дни работают: " + not_even)

 # Вариант №3: Питон сам определяет чет и не чет из списка
 
oll_workers = [NAME_1, NAME_2, NAME_3, NAME_4]
even = oll_workers[::2]
not_even = oll_workers[1::2]
print("В чётные дни работает: ", even, 
      "\n "
      "\nВ нечётные дни: ", not_even)