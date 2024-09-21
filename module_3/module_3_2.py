test_list = ['сообщение для проверки', 'НЕ АДРЕС',
             'Это сообщение для проверки связи', 'vasyok1337@gmail.com',
             'Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', " sender = 'urban.info@gmail.com' ",
             'Пожалуйста, исправьте задание', 'urban.student@mail.ru', " sender = 'urban.teacher@mail.uk' ",
             'Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', " sender = 'urban.teacher@mail.ru' "]


def test():
    print('____________________________________________________________________________________')
    print('test --->  send_mail', '\n')
    print('START_______________________________________________________________________________')
    send_mail('сообщение для проверки', 'НЕ АДРЕС')
    send_mail('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
    send_mail('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
    send_mail('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
    send_mail('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
    print('END_________________________________________________________________________________')


def send_mail(message, recipient, sender="university.help@gmail.com"):
    if not (is_com(recipient) and is_com(sender)):
        print(f'Невозможно отправить письмо с адреса "{sender}" на адрес "{recipient}".')
    elif (recipient == sender):
        print(f'"Нельзя отправить письмо самому себе!"')
    elif (sender == 'university.help@gmail.com'):
        print(f'"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."')
    else:
        print(f'"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


def is_com(address):
    address = str(address)
    address_is_com = False
    if (address.find('@') == -1):
        return address_is_com

    valid_com = [".com", ".ru", ".net"]
    for i in range(len(valid_com)):
        address_is_com = address.endswith(valid_com[i])
        if address_is_com:
            break
    return address_is_com


test()
