"""
В данной задаче (12_2), допущена логическая ошибка.
Попробуйте решить эту проблему и обложить дополнительными тестами.
"""
"""
Исправленно несколько конфликтных ситуаций:
    1 Дистанция забега меньше либо равна нулю.
    2 Скорость одного или нескольких бегунов меньше либо равна нулю.
    3 Порядок обработки списка бегунов в классе не должен влиять на результат забега.
    4 Скорость двух или более бегунов превышает длину дистанции забега.
    5 Скорость двух или более бегунов одинакова или два или более бегуна/ов финишируют одновременно.
    6 Прочие специфические поправки.
"""


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        # Исправленно: Скорость участника не может быть меньше либо равна нулю.
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость бегуна равна "{speed}"')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        # Исправленно: Не можем начать забег если дистанция забега меньше либо равна нулю.
        if distance > 0:
            self.full_distance = distance
        else:
            raise ValueError(f'Дистанция забега равна "{distance}"')
        # Исправленно: теперь принимает разные типы данных списока участников
        # tuple(a, b, c) или list[a, b, c] или a, b, c
        self.participants = []
        for user in participants:
            if isinstance(user, Runner):
                self.participants = [x for x in participants]
                break
            elif isinstance(user, tuple):
                self.participants = list(user)
                break
            elif isinstance(user, list):
                self.participants = user
                break
            else:
                raise ValueError(f'Неверный тип данных в списке участников забега!')

    def start(self):
        count_participants = len(self.participants)
        finishers = {}
        place = 0
        # Исправленно: если в забеге участвует бегун self.distance которого (!= 0)
        # возникнет искажение результата забега
        # или "вечный цикл" т.к. count_participants не достигнет ноля,
        # поэтому обнуляем self.distance каждого участника
        for index in range(len(self.participants)):
            self.participants[index].distance = 0
        #
        # Забег
        while count_participants > 0:
            span = []
            # "Рывок" это вынужденная абстракция имитирующая равные промежутки времени из-за
            # отсутствия привязки забегов к настоящим отрезкам времени,
            # т.к. имеем только аргумент self.speed
            for runner in self.participants:
                # Один "рывок" для каждого бегуна из списка участников забега
                if runner.distance >= self.full_distance:
                    # Если участник забега уже финишировал, пропустим его
                    continue
                else:
                    # "Рывок"
                    runner.run()
                    if runner.distance >= self.full_distance:
                        # Если есть финишировавший бегун на "рывке" добавим его в список span
                        span.append(runner)
                        # Уменьшим счетчик оставшихся бегунов на единицу
                        count_participants -= 1
            # Если после очередного "рывка" есть финишировавший/ие
            if len(span) > 0:
                place += 1
                # Назначим место финишировавшим на данном "рывке"
                finishers[place] = span
        return finishers
