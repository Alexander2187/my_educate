class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = int(start)
        self.stop = int(stop)
        self.step = int(step)
        self.pointer = self.start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        step_pointer = abs(self.step)
        current_pointer = self.pointer
        new_pointer, end = 0, 0
        if self.start == self.stop or step_pointer == 0:
            raise StepValueError
        elif self.start < self.stop:
            new_pointer = current_pointer + step_pointer
            end = range(self.stop, self.stop + step_pointer + 1)
        elif self.start > self.stop:
            new_pointer = current_pointer - step_pointer
            end = range(self.stop - step_pointer, self.stop)
        if new_pointer in end:
            if self.pointer == self.stop:
                raise StopIteration
            else:
                self.pointer = self.stop
                return current_pointer
        else:
            self.pointer = new_pointer
            return current_pointer


if __name__ == '__main__':
    print("------------------>  if __name__ == '__main__'  <------------------")
    try:
        iter1 = Iterator(100, 200, 0)
        for i in iter1:
            print(i, end=' ')
    except StepValueError:
        print('Шаг указан неверно')

    iter2 = Iterator(-5, 1)
    iter3 = Iterator(6, 15, 2)
    iter4 = Iterator(5, 1, -1)
    iter5 = Iterator(10, 1)

    for i in iter2:
        print(i, end=' ')
    print()
    for i in iter3:
        print(i, end=' ')
    print()
    for i in iter4:
        print(i, end=' ')
    print()
    for i in iter5:
        print(i, end=' ')
    print()
