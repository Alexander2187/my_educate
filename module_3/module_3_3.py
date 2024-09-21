def test():
    print('____________________________________________________________________________________')
    print('test --->  print_params', '\n')
    print('START_______________________________________________________________________________')
    print_params()
    print_params(b=25)
    print_params(c=[1, 2, 3])
    print_params(*values_list)
    print_params(*values_dict)
    print_params(*values_list_2, 42)
    print('END_________________________________________________________________________________')


values_list = ['"Число"', 3.14, True]
values_dict = {'a': '"First"', 'b': 0.125, 'c': 125_000}
values_list_2 = ['Value', False]


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


test()
