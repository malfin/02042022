numbers = input()
summa = 0

'''

Оборачиваем в список, берём встроенную функцию map() ->
      int - числовой тип данный ->
      добавляем строчный тип данных (str), сплитим его по ","

'''

numbers_list = list(map(int, numbers.split(',')))

'''

Через цикл for вычитаем данные (-=)

'''

for i in numbers_list:
    summa -= i

print(summa)
