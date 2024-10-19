from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    count = 0

    with open(file_name, 'w', encoding='utf-8') as text_IO:
        for index in range(word_count):
            count += 1
            label = f"Какое-то слово № {count}\n"
            text_IO.write(label)
            sleep(0.1)
    print(f'"Завершилась запись в файл {file_name}"')


start_time = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = datetime.now()
print(end_time - start_time)

start_time = datetime.now()

a = Thread(target=write_words, args=(10, 'example5.txt'))
b = Thread(target=write_words, args=(30, 'example6.txt'))
c = Thread(target=write_words, args=(200, 'example7.txt'))
d = Thread(target=write_words, args=(100, 'example8.txt'))

a.start()
b.start()
c.start()
d.start()

a.join()
b.join()
c.join()
d.join()

end_time = datetime.now()
print(end_time - start_time)
