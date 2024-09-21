def test():
    print('____________________________________________________________________________________')
    print('test --->  single_root_words', '\n')
    print('START_______________________________________________________________________________')
    print(single_root_words('rich', 'richiest', 'orich', 'orichalcum', 'cheers', 'richies'))
    print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
    print('END_________________________________________________________________________________')


def single_root_words(root_word, *other_words):
    root_word = str(root_word).lower()
    same_words = []

    for i in range(len(other_words)):
        other_w = str(other_words[i]).lower()

        # Ищем ключевое слово в списке слов
        is_single_root = not (other_w.find(root_word) == -1)
        if is_single_root:
            same_words.append(other_words[i])
            continue

        # Ищем каждое слово из списка в ключевом слове
        is_single_root = not (root_word.find(other_w) == -1)
        if is_single_root:
            same_words.append(other_words[i])
            continue

    return same_words


test()
