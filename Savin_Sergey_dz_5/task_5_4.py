print('Hello World')


src =  [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0]
print(my_list)