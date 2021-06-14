import sys

show_sales = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as f:
    if len(show_sales) > 1:
        start_idx = int(show_sales[0])
        end_idx = int(show_sales[1])
    elif len(show_sales) == 0:
        start_idx = 0
        end_idx = sum(1 for line in f)
        f.seek(0)
    else:
        start_idx = int(show_sales[0])
        end_idx = sum(1 for line in f)
        f.seek(0)

    for idx, line in enumerate(f):
        if start_idx <= idx + 1 <= end_idx:
            print(line.strip())
