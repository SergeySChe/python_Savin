print('Hello World')

prices = [57.8, 23.45, 17.18, 45.16, 32.23, 55.6, 22.11, 67.89, 1.1, 23.3]

for price in prices:
    rub = int(price)
    kk = (price - rub) * 100
   # print(f'{rub} руб {kk:02.0f}коп')

for price in sorted(prices)[::-1][:5]:
    rub = int(price)
    kk = (price - int(price)) * 100
   # print(f'{int(price)} руб {kk:02.0f} коп')

print([f'{int(price)} руб {(price - int(price)) * 100:02.0f} коп' for price in sorted(prices)[::-1][:5]])
