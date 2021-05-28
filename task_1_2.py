print('Hello World')

number = [i ** 3 for i in range (1, 1001, 2)]

totals = 0

for num in number:
    sum = 0
    end_number = num
    while end_number > 0:
        sum += end_number % 10
        end_number = end_number // 10
    if sum % 7 == 0:
        totals += num
print(totals)

total_two = 0
for num in number:
    num += 17
    sum = 0
    end_number = num
    while end_number > 0:
        sum += end_number % 10
        end_number = end_number // 10
    if sum % 7 == 0:
        total_two += num
print(total_two)
