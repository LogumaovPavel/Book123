from inteface import *
from algoritm import *

while True:
    interface()
    command = int(input('Введите команду: '))
    if command==1:
        person = input("Введите данные пользователя ")
        add_person(person)      
    elif command==2:        
        show_all()
    elif command==3:
        name = input("Введите элемент для поиска: ")
        search_element(name)  
    elif command==4:
        num = int(input("введите номер строки, которую хотите отредактировать: "))
        new = input("введите новую строку: ")
        edit_string_in_file(num, new)        
    elif command ==5:
        surname = input("введите данные: ")
        delete_line(surname)            
    elif command == 6:
                break        
    else:
        print("Ввод некорректен")