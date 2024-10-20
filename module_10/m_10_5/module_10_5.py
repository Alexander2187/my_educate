import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as textIO:
        x = 'some_length'
        while len(x) > 0:
            x = textIO.readline()
            all_data.append(x)


if __name__ == '__main__':
    print("------------------>  if __name__ == '__main__'  <------------------")

    #  Line
    start_time = datetime.now()
    for index in range(4):
        read_info(f'file {index + 1}.txt')
    end_time = datetime.now()
    print(f"Линейно:     {end_time - start_time}")

    #  Multiprocessing
    start_time = datetime.now()
    with multiprocessing.Pool(processes=8) as pool:
        all_files = []
        for index in range(4):
            all_files.append(f'file {index + 1}.txt')
        pool.map(read_info, all_files)
    end_time = datetime.now()
    print(f"Параллельно: {end_time - start_time}")
