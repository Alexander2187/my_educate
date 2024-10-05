def custom_write(file_name, strings):
    #
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = dict()
    count_lines = 0
    for item in strings:
        count_lines += 1
        strings_positions[(count_lines, file.tell())] = item
        file.write(item + '\n')
    return strings_positions


if __name__ == '__main__':

    s = ['The Python interpreter',
         'raises an exception',
         'when it detects',
         'run-time error',
         '(such as division by zero).']

    result = custom_write('test.txt', s)
    for elem in result.items():
        print(elem)

    # info = ['Text for tell.',
    #         'Используйте кодировку utf-8.',
    #         'Because there are 2 languages!',
    #         'Спасибо!']
    #
    # result = custom_write('test.txt', info)
    # for elem in result.items():
    #     print(elem)