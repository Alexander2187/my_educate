immutable_var = (3140, 18.145, 'numbers', [42, True])
print(immutable_var, '  <-- Неизменяемый кортеж')

#   Так не сработает:
#   immutable_var[2] = 58  <-- Этот код вызовет ошибку:
#   "TypeError: 'tuple' object does not support item assignment"
#   так-как кортеж эвляется неизменяеммым типом данных.

mutable_list = ['2', 25, 'Python', True]
print(mutable_list, '   <-- Изменяемый список')

mutable_list[1] = 498
print(mutable_list, '   <-- Изменён второй элемент списока')
