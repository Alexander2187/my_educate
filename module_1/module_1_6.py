#   Работа со словарями:
my_dict = {'Владислав': 45, 'Егор': 16, 'Антонина': 32}
print('\n''Словать: -->     ', my_dict)

print("Существующий ключ: 'Егор' -->    ", my_dict.get('Егор'))
print("Несуществующий ключ: 'Иван' -->    ", my_dict.get('Иван', 'В словаре нет такого имени'))

my_dict.update({'Арина': 19, 'Максим': 51})

delite_value = my_dict.pop('Егор')
print("Удаленное значение: 'Егор' -->    ", delite_value)
print('Изменённый словарь: -->    ', my_dict, '\n')


#   Работа с множествами:
my_set = {20, 45, 20, 45, 71, True, True, 'Jon', 'Alisa','Jon', 3.14}
print('Множество: -->    ', my_set)

my_set.add(False)
my_set.add('Antonio')

my_set.discard(3.14)
print('Изменённое множество: -->    ', my_set)