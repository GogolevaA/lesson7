# from name import get_name
# from loger import write_cvc, read_cont, write_txt
# def click():
#     while 1>0:
#         print('1-добавить ученика\n 2. поставить оценку\n 3.я ученик и хочу просмотреть свои оценки')
#         a=int(input())
#         if a==1:
#             get=get_name()
#             write_cvc(get)
#             write_txt(get)
#         elif a==2:
#             print(read_cont())
#         elif a==3:   
#             break 
#         else:
#             print('введено неккорктное значение')

        
from tach import add_stud, get_name
from stud_baza import save_db, load_db
from sduds import see_mark

def click():
    load_db()
    while 1>0:
        print('1-я учитель\n 2. я ученик')
        c=int(input())
        if c==1:
           print('1-добавить ученика\n 2. поставить оценку\n 3. закончить работу')
           a=int(input())
           if a==1:
            add_stud()
           elif a==2:
            get_name()
           elif a==3:   
            break 
           else:
            print('введено неккорктное значение')
        elif c==2:
            last_name=input('введите свою фамилию или 3 выйти\nввод: ')
            if last_name==3:
                break
            else:
                see_mark(last_name)


