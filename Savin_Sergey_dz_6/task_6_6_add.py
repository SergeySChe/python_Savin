import sys

add_sale = sys.argv[1:]

with open('bakery.csv', 'a', encoding='utf-8') as f:
    add_sale = f'{add_sale}\n'
    f.write(add_sale)
