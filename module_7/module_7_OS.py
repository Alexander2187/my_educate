import os, time


def any_dir_walk(any_parent_dir):
    for root, dirs, files in os.walk(any_parent_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_time = os.path.getmtime(file_path)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
            file_size = os.path.getsize(file_path)
            parent_dir = os.path.dirname(file_path)
            print(f'Обнаружен файл: {file},\n '
                  f'Путь: {file_path},\n '
                  f'Размер: {file_size} байт,\n '
                  f'Время изменения: {formatted_time},\n '
                  f'Родительская директория: {parent_dir}\n')


if __name__ == '__main__':
    print("------------------>  if __name__ == '__main__'  <-----------------------------------")

    directory = r'.'
    any_dir_walk(directory)

    # for root, dirs, files in os.walk(directory):
    #     print(f'\n for Root  -->[ {root}], '
    #           f'\n    Dirs  -->[ {dirs}], '
    #           f'\n    Files -->[ {files}] in os.walk(directory)\n')
    #     for file in files:
    #         print(f'        for_File --> [{file}] in files:')
    #         file_real_path = os.path.realpath(file)
    #         print(f'            {file_real_path}\n')
