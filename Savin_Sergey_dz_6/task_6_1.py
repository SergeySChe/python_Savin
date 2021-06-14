print('Hello World')

with open('nginx_logs.txt') as f:
    adress = []
    for line in f:
        splitted = line.split()
        adress.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
print(adress)
