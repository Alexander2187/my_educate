def apply_all_func(int_list, *functions):
    results = dict()
    for func in functions:
        try:
            results[func.__name__] = func(int_list)
        except TypeError:
            print(f'Аргументы для "{func.__name__}" не соответствуют требованиям!')
    return results


if __name__ == '__main__':
    print("------------------>  if __name__ == '__main__'  <------------------")
    print(apply_all_func([6, 20, 15, 9], len, max, min, sum, sorted))
    print()
    print(apply_all_func([6, -2.0, (5.0, 0.2), 9], len, max, min, sum, sorted, int))
