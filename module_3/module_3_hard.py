# Exercise data
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# Modified data
my_test_data = [
    [1, 2, 3, True, False],
    {'a': 4, 'b': 5},
    (6, {'c4 e': 7, ';:\'\"': 8}),
    'He(}o',
    ((), [{(2, 'U[]an', ('}(]{)[', 30.0, 5.0))}])
]


def test():
    print('____________________________________________________________________________________')
    print('test --->  calculate_structure_sum', '\n')

    print('START_______________________________________________________________________________')
    print('IF BOOL ', calculate_structure_sum(True))
    print('IF INT ', calculate_structure_sum(10_123))
    print('IF FLOAT ', calculate_structure_sum(3.1415))
    print('IF STRING ', calculate_structure_sum("This is String, len(23)"))

    print('my_test_data________________________________________________________________________')
    print(calculate_structure_sum(my_test_data))

    print('data_structure______________________________________________________________________')
    result = calculate_structure_sum(data_structure)
    print(result)

    print('END_________________________________________________________________________________')


count = 0


def calculate_structure_sum(data_structure):
    # Счетчик вернет (сумму всех чисел + кол-во всех букв)
    count = 0
    dt = data_structure
    #   Игнорирует любые значения типа Boolean
    if isinstance(dt, bool):
        return 0

    elif isinstance(dt, str):
        count += len(dt)
        return count

    elif isinstance(dt, int) or isinstance(dt, float):
        count += dt
        return count

    elif isinstance(dt, list) or isinstance(dt, tuple):
        for item in range(len(dt)):
            count += calculate_structure_sum(dt[item])
        return count

    elif isinstance(dt, set) or isinstance(dt, frozenset):
        for item in dt:
            count += calculate_structure_sum(item)
        return count

    elif isinstance(dt, dict):
        for key in dt:
            count += calculate_structure_sum(key)
            count += calculate_structure_sum(dt.get(key))
        return count
    else:
        return 0
    return count


test()
