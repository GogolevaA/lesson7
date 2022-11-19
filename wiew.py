from name import get_name
from loger import write_cvc, read_cont, write_txt
def click():
    while 1>0:
        print('1-добавить контакт\n 2. показать справочник\n 3.Выйти из спрвочника')
        a=int(input())
        if a==1:
            get=get_name()
            write_cvc(get)
            write_txt(get)
        elif a==2:
            print(read_cont())
        elif a==3:   
            break 
        else:
            print('введено неккорктное значение')

        



