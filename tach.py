from stud_baza import set_stud, set_mark

def add_stud():
    data=input('введитите данные (фамилияб имяб класс через пробел):').split(' ')
    set_stud(data)
 
def get_name():
    last_name=input('ввкдите фамилию: ')
    lesson=input('введите предмет: ')
    mark=input('введите оценку').split()
    set_mark(last_name,lesson,mark)