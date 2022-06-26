# Пятый модуль

dr_pushkin = None
dr_user = None
while dr_pushkin != 1799:
    dr_pushkin = int ( input('Введите год рождения Пушкина'))
    if dr_pushkin != 1799:
        print('Не верный год рождения')
else:
    while dr_user != 2007:
        dr_user = int(input ('Введите ваш день рождения'))
        if dr_user != 2007:
            print('Не верный день рождения')
    else:
            print('Верный день рождения!')

