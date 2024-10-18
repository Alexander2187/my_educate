def is_prime(f):
    def wrapper(*args):
        var = f(*args)
        if var % 2 == 0:
            print("Составное")
            return var
        d = 3
        while d * d <= var and var % d != 0:
            d += 2
        if d * d > var:
            print("Простое")
            return var
        else:
            print("Составное")
            return var
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


if __name__ == '__main__':
    print("------------------>  if __name__ == '__main__'  <------------------")

    print(sum_three(1, 4, 6))
    print(sum_three(2, 4, 6))
    print(sum_three(3, 4, 6))

