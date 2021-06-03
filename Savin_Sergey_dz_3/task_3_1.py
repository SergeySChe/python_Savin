print('Hello World')

number_list = {'one': 'один',
          'two': 'два',
          'three': 'три',
          'four': 'четыре',
          'five': 'пять',
          'six': 'шесть',
          'seven': 'семь',
          'eight': 'восемь',
          'nine': 'девять',
          'ten': 'десять'}


def num_translate(eng):
    return number_list.get(eng)

print(num_translate('five'))






