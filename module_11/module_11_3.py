""" Introspection """


class My_intro_test(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def any(self):
        return 'U-u-psss'


def introspection_info(some_obj):
    log = {}
    log['type'] = type(some_obj)
    if some_obj.__getstate__() is None:
        log['attributes'] = []
    else:
        log['attributes'] = [key for key in some_obj.__getstate__()]
    log['methods'] = [x for x in dir(some_obj) if x not in log['attributes']]
    log['module'] = some_obj.__class__.__module__
    return log


if __name__ == '__main__':
    print("------------------>  if __name__ == '__main__'  <------------------")

    tm = My_intro_test(1, 2, 3)
    number_info = introspection_info(42)
    x = number_info
    for key in x:
        print(key, x[key])
