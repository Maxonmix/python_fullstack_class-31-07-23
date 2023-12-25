import statistics as st

a = list(map(int, input("Введите цены: ").split(',')))
b = st.mean(a)
print("Средняя цена товара: ", b)