# Input data:
# names_list = ['Bob', 'Angel', 'Jimi', 'Alan', 'Ada']  --> not more than 5 names
# input names (alphabet symbols only): e.g. Bob, Angel, Jimi, Alan, Ada
# Output data:
# file that contains names
names_list = []

while True:
    try:
        name = input('Input name: ')
        if name.lower() == 'stop':
            raise BaseException('You have entered Stop')
        if not name.isalpha():
            raise TypeError
        if len(names_list) == 5:
            print('The list is full, no more names can be added')
            break
        names_list.append(name)

    except TypeError:
        print("Name should contain only letters")
    except BaseException:
        names_list.clear()
        print('Y`ve entered Stop!')
        raise ValueError('Do not enter Stop please')

try:
    with open('names.txt', 'w', encoding='utf-8') as file:
        for name in names_list:
            file.write(f'{name}\n')
except FileNotFoundError:
    print('File not found')
