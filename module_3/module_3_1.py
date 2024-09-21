calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    str_len = len(str(string))
    str_upr = str(string).upper()
    str_low = str(string).lower()
    tuple_str = (str_len, str_upr, str_low)
    return tuple_str


def is_contains(string, list):
    count_calls()
    is_str_in_list = False
    st_x = str(string).lower()
    for i in range(len(list)):
        buf = str(list[i]).lower()
        is_str_in_list = (buf.find(st_x) != -1)
        if is_str_in_list:
            break

    return is_str_in_list


print(is_contains('WeR', ['awErt', 'yTtghj']))
print(is_contains('10', ['aw10rt', 'yTtghj']))
print(string_info('10GGjjb gjhfghvjwawWAW DxfEXtcggvtRRERXECvgg bvG87b698 noom,kl_)+_)(*&678'))

print(calls)
