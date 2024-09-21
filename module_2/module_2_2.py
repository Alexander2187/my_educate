from idlelib.configdialog import is_int

print('Сравнение трёх целых чисел на равенство')

count_numbers = 0
list_numbers = [0, 0, 0]

while (count_numbers < 3):
    print('Введите целое число:')
    x = input()

    if len(x) == 0:
        print('Пустой ввод')
        continue
    elif is_int(x):
        list_numbers[count_numbers] = x
        count_numbers = count_numbers + 1
        print('Ок\n' + str(count_numbers) + '-е число введено успешно\n')
    else:
        print("Невернный ввод!\nПо крайней мере один из введённых знаков не является цифрой\n")
        continue
        print('TEST')

first = list_numbers[0]
second = list_numbers[1]
third = list_numbers[2]

if (first == second and second == third):
    print(3, 'Все три числа равны')
elif (first != second and second != third and first != third):
    print(0, 'Числа не равны')
else:
    print(2, 'Два числа равны')
