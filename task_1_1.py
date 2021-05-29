print('hello world')


mine = 60
hor = 3600
day = 86400
user_duration = int(input('введите число: '))

if user_duration < mine:
    print(user_duration, 'сек')
elif user_duration < hor:
    my_mine = user_duration // mine
    my_sec = user_duration % mine
    print(my_mine, 'мин', my_sec, 'сек')
elif user_duration < day:
    my_hor = user_duration // hor
    my_mine = user_duration % hor // mine
    my_sec = user_duration % hor % mine
    print(my_hor, 'час', my_mine, 'мин', my_sec, 'сек')
elif user_duration >= day:
    my_day = user_duration // day
    my_hor = user_duration % day // hor
    my_mine = user_duration % day % hor // mine
    my_sec = user_duration % day % hor % mine
    print(my_day, 'дн', my_hor, 'час', my_mine, 'мин', my_sec, 'сек')

