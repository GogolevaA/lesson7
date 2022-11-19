from name import get_name as name

def write_cvc(name):
    file='phonebook.cvc'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'фамилия: {name[0]}; имя: {name[1]}; номер: {name[2]}\n')

def read_cont():
    with open('phonebook.cvc', 'r', encoding='utf-8') as r:
        return r.read()

def write_txt(name):
    file='phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'фамилия: {name[0]}\n имя: {name[1]}\n номер: {name[2]}\n\n')