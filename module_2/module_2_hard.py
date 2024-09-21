#   Алгоритм подбора шифра.
def decode(x):
    # 1. Найти список делителей в порядке возрастания.
    div_x = []
    for i in range(x):
        if i == 0:  # Убираем из делителей "1".
            continue
        is_div = (x % (i + 1)) == 0
        if is_div:
            div_x.append(i + 1)

    # 2. Разобрать список делителей [a, b, c] на сумму уникальных пар чисел (f, s),
    #    по одной паре на список делителей за раз,
    #    например: [f_a,  s_a,  f_b,  s_b,  f_c,  s_c,
    #               f1_a, s1_a, f1_b, s1_b, f1_c, s1_c,
    #               f2_a, s2_a, f2_b, s2_b, f2_c, s2_c,
    #               и т.д.].
    # 3. Исключить из списка делителей число,
    #    если образованная пара соответствует условию (f == s or f > s)
    # 4. Повторять пункты 2-3 до тех пор пока не останется ни одного делителя.
    pair_num = []
    f = 0
    s = 0
    growth = 1
    have_div = len(div_x) > 0
    while have_div:  # 2.
        for i in range(len(div_x)):
            f = growth
            s = (div_x[i] - growth)
            if (f == s or f > s):  # 3.
                delited = div_x.pop(i)
                growth = growth - 1
                break
            else:
                pair_num.append(f)
                pair_num.append(s)
        growth = growth + 1
        if len(div_x) <= 0:
            have_div = False

    # 5. Конвертировать список пар в монолитное число.
    result = ''
    for i in range(len(pair_num)):
        result = result + str(pair_num[i])
    result = int(result)
    return result

print(decode(13))