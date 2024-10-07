from time import sleep


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)


class UrTube:
    def __init__(self):
        self.users = dict()  # (список объектов User)
        self.videos = dict()  # (список объектов Video)
        self.current_user = None

    def __check_nick(self, user_input):
        if isinstance(user_input, str):
            # not empty, not number, not string with spaces
            if (len(user_input) > 0) and (not user_input.isdigit()) and not (1 + user_input.find(' ')):  #
                nickname = user_input
                return nickname
            else:
                print(f'This name --> "{user_input}" <-- is "empty" or "number" or "string with spaces"')
                return False
        else:
            print(f'This name --> "{user_input}" <-- is not type String')
            return False

    def __check_pass(self, user_input):
        if isinstance(user_input, str):
            # not empty, not string with spaces
            if (len(user_input) > 0) and not (1 + user_input.find(' ')):
                password = user_input
                return password
            else:
                print(f'This password is "empty" or "number" or "string with spaces"')
                return False
        else:
            print(f'This password is not type String')
            return False

    def __check_age(self, user_input):
        user_input_str = str(user_input)
        if user_input_str.isdigit():
            age = int(user_input_str)
            if age in range(1, 200):
                return age
            else:
                print(f'This age --> "{age}" <-- is out of Range(1 - 200)')
                return False
        else:
            print(f'This age --> "{user_input_str}" <-- is not type Integer')
            return False

    def __check_user(self, users, nickname, password):
        for user in users:
            if user == nickname:
                if users[user].password == hash(password):
                    return True
                else:
                    return False
            else:
                continue
        return False

    def __find_user(self, users, nickname):
        for user in users:
            if user == nickname:
                return True
            else:
                continue
        return False

    def register(self, nickname, password, age):
        """
        Принимает три аргумента: nickname, password, age,
        и добавляет пользователя в список, если пользователя не существует (с таким же nickname).

        Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически.
        """
        if self.__check_nick(nickname) and self.__check_pass(password) and self.__check_age(age):
            if self.__find_user(self.users, nickname):
                print(f'Пользователь {nickname} уже существует!')
            else:
                self.users[nickname] = User(nickname, password, age)
                self.current_user = nickname
                # print(f"{len(self.users)} Регистрация {nickname} прошла успешно, вход выполняется автоматически!")
        else:
            print(f'Некорректный ввод!')

    def log_in(self, nickname, password):
        """
        Принимает на вход аргументы: nickname, password
        и пытается найти пользователя в users с такими же логином и паролем.

        Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу.
        """
        if self.__check_nick(nickname) and self.__check_pass(password):
            if self.__check_user(self.users, nickname, password):
                self.current_user = nickname  # current_user меняется на найденного.
                print(f"Авторизация {nickname} прошла успешно!")
            else:
                print(f'Неверное имя пользователя или пароль!')
        else:
            print(f'Некорректный ввод!')

    def log_out(self):
        """ Для сброса текущего пользователя на None.
        """
        self.current_user = None

    def add(self, *args):
        """
        Принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
        """
        for arg in args:
            if arg in self.videos:
                continue
            else:
                self.videos[arg.title] = arg

    def get_videos(self, search_word):
        """
        Принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
        Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
        """
        find_titles = list()
        for key in self.videos:
            title = self.videos[key].title
            low_title = title.lower()
            word = search_word.lower()
            if (-1) != low_title.find(word):
                find_titles.append(title)
        return find_titles

    def watch_video(self, title):
        """
        Принимает название фильма,
        если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится,
        если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.

        После текущее время просмотра данного видео сбрасывается.
        """
        find_video = False
        current_video = None
        for key in self.videos:
            if key.lower() == title.lower():
                find_video = True
                current_video = self.videos[key]
                break

        if find_video:
            if self.current_user:
                if ((self.users[self.current_user].age >= 18)
                        or (self.users[self.current_user].age < 18) and (not current_video.adult_mode)):
                    for i in range(current_video.duration):
                        current_video.time_now = i + 1
                        print(current_video.time_now, end=' ')
                        sleep(1)
                    print('Конец видео')
                    current_video.time_now = 0
                else:
                    print(f'"Вам нет 18 лет, пожалуйста покиньте страницу"')
            else:
                print(f'"Войдите в аккаунт, чтобы смотреть видео"')


if __name__ == '__main__':
    print("\n---------------------------------------------------------------------------")
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
    print("\n---------------------------------------------------------------------------")