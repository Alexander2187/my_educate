class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        pass

    def get_all_words(self):
        """
        Алгоритм получения словаря вида:
            {'file1.txt': ['word1', 'word2'],
            'file2.txt': ['word3', 'word4'],
            'file3.txt': ['word5', 'word6', 'word7']}
        Где:
            'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
            ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.

        :return: Словарь all_words: ключ - название файла, значение - список слов из этого файла.
        """
        all_words = dict()
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as text_io:
                text = text_io.read()
            # File is close
            """Алгоритм очистки и разделения теста на отдельные слова"""
            word = ''
            words_from_file = []
            garbage_chars = [',', '.', '=', '!', '?', ';', ':', ' - ']
            separator_char = ['-', ' ', '\n']
            # Universal For All
            for index in range(len(text)):
                char = text[index].lower()
                if char in garbage_chars:
                    """Пропускаем не нужные символы"""
                    continue
                elif char in separator_char:
                    """Нашли разделительный символ? -> добавим слово в список"""
                    if word != '':
                        words_from_file.append(word)
                    word = ''
                else:
                    """Собираем слово из символов"""
                    word += char
            # Special For Last
            if word != '':
                """Добавим последнее слово, если оно есть."""
                words_from_file.append(word)
            #
            """Словарь all_words: 
                ключ - название файла, 
                значение - список слов из этого файла."""
            all_words[name] = words_from_file
        return all_words

    def find(self, word):
        """
        :param word: Искомое слово.
        :return: Словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
        """
        word = word.lower()
        result_find = dict()
        all_words = self.get_all_words()
        for key in all_words:
            position = None
            for index in range(len(all_words[key])):
                if word == all_words[key][index]:
                    position = index + 1
                    break
            if isinstance(position, int):
                result_find[key] = position
            else:
                result_find[key] = 'Отсутствует'
        return result_find

    def count(self, word):
        """
        :param word: Искомое слово.
        :return: Словарь, где ключ - название файла, значение - количество слов word в списке слов этого файла.
        """
        word = word.lower()
        result_count = dict()
        all_words = self.get_all_words()
        for key in all_words:
            count = 0
            for index in range(len(all_words[key])):
                if word == all_words[key][index]:
                    count += 1
            result_count[key] = count
        return result_count


if __name__ == '__main__':
    f = WordsFinder('Я помню чудное мгновенье.txt', 'У лукоморья дуб зелёный.txt')
    x = f.get_all_words()
    for key in x:
        print(key, x[key])

    find_word = 'коТ'

    x = f.find(find_word)
    for key in x:
        print(key, x[key])

    x = f.count(find_word)
    for key in x:
        print(key, x[key])
