print('Hello World')

name_colleague = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for number in name_colleague:
    print('Привет ', number.split()[-1].title())