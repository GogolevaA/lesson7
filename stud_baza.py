import json
import os

def set_stud(data_list):
    stud_db[data_list[0]]=data_list[1:],{}

def set_mark(last_name, lesson, mark):
    if stud_db.get(last_name) is None:
        print(f'фамилия {last_name} не найдена')
        print(stud_db)
    else:
        if lesson in stud_db[last_name][1]:
            stud_db[last_name][1][lesson].extend(mark)
        else:
            stud_db[last_name][1][lesson]=mark

def get_stud(last_name_stud):
    if stud_db.get(last_name_stud) is None:
        print(f'фамилия {last_name_stud} не найдена')
    else:
        data=stud_db[last_name_stud]
        print(f'{last_name_stud} {", ".join(data[0])}:')
        print(*[f'{key}: {", ".join(value)}' for key, value in data[1].items()], sep='\n')

def save_db():
    json.dump(stud_db,open('db_stud.json', 'w'))

def load_db():
    global stud_db
    if os.stat('db_stud.json').st_size == 0:
        stud_db={}
    else:
        stud_db=json.load(open('db_stud.json'))

