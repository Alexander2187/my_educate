def sample_format():
    team_name_1 = 'Мастера кода'
    team_name_2 = 'Волшебники данных'
    team1_num = 5
    team2_num = 6
    score_1 = 40
    score_2 = 42
    team1_time = 1552.512
    team2_time = 2153.31451
    tasks_total = 82
    time_avg = 45.2

    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = f'Победа команды {team_name_1}!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = f'Победа команды {team_name_2}!'
    else:
        result = 'Ничья!'
    challenge_result = result

    #
    """ Sample interpolation operator (%), or modulo operator
    """
    print('"В команде %s участников: %s !"' % (team_name_1, team1_num))
    print('"Итого сегодня в командах участников: %s и %s !"' % (team2_num, team1_num))

    #
    """ Sample str.format() method
    """
    print('"Команда {0} решила задач: {1} !"'.format(team_name_2, score_2))
    print('"{} решили задачи за {} с !"'.format(team_name_2, team2_time))

    #
    """ Sample F-sting 
    """
    print(f'"Команды решили {score_1} и {score_2} задач.”')
    print(challenge_result)
    print(f'"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."')


sample_format()
