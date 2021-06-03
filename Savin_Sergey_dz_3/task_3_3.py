print('Hello World')


def thesaurus(*names):
    my_names = dict()
    for name in names:
        my_names.setdefault(name[0], [])
        my_names[name[0]].append(name)
    return my_names


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
