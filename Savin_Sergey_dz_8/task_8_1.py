print('Hello World')


import re
EMAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')
def email_parse(email):
    found_info = EMAIL.findall(email)[0]
    if found_info:
        name, addr = found_info
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, addr)

email_parse('sergeysche88@mail.ru')
