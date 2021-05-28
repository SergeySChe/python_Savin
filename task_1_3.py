print('Hello World')

perc_grup = ['процент', 'процента', 'процентов']
numbers_grup = [i for i in range (1, 21)]

#user = int(input('введите число от 1 до 20: '))

for number in numbers_grup:
    if number == 1:
        print(number, perc_grup[0])
    elif number < 5:
        print(number, perc_grup[1])
    else:
        print(number, perc_grup[2])

