print('Hello World')


def odd_number(max):
    n = 1
    while n <= max:
        yield n
        n += 2


odd_to_15 = odd_number(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
