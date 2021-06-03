print('hello World')

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def jokes_finish(num):
    """ May the force be with you! """
    my_list = []
    for i in range(num):
        my_nouns = random.choice(nouns)
        my_adverbs = random.choice(adverbs)
        my_adjectives = random.choice(adjectives)
        my_list.append(f'{my_nouns} {my_adverbs} {my_adjectives}')
    return my_list


print(jokes_finish(2))