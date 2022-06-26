# Третий модуль

dr_pushkin = None
dr_user = None
dr_pushkin = int ( input('Введите год рождения Пушкина'))
if dr_pushkin == 1799:
    dr_user = int(input ('Введите ваш день рождения'))
    if dr_user == 2007:
        print('Верный день рождения!')
    else:
        print('Не верный день рождения')
else:
    print('Не верный год рождения')


