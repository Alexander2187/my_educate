def all_variants(text):
    is_letter = False
    if len(text) > 0:
        is_letter = True
    while is_letter:
        for index in range(len(text)):
            """ На каждой итеррации цикла 
            возвращаем срез, который короче предыдущего 
            на одну букву с конца строки. 'abcd', 'abc', 'ab', 'a'.
            """
            yield (text[0:len(text) - index])
        if len(text) > 0:
            is_letter = True
            """ Убираем одну букву с начала строки.  'abcd' -> 'bcd' """
            text = text[1:]
        else:
            is_letter = False


if __name__ == '__main__':
    print("------------------>  if __name__ == '__main__'  <------------------")
    
    a = all_variants("abc")
    for i in a:
        print(i)

    a = all_variants("Watermelon")
    for i in a:
        print(i)
