def add_person(person):
    data = open('Dict.txt', 'a', encoding = 'utf-8' )
    data.write(person)
    data.write('\n')
    data.close()

def show_all():
    data = open ('Dict.txt', 'r', encoding = 'utf-8' )
    for line in data:
        print(line[:-1])
    data.close()

def search_element(name):
    with open ('Dict.txt', 'r', encoding = 'utf-8' ) as data:
        for line in data:
            if name in line.split():
                print(line)
                break
        else:
            print('Элемент отсутствует')
def edit_string_in_file(line_number, new_string):
    with open('dict.txt', 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
    if line_number >= 1 and line_number <= len(lines):
        lines[line_number - 1] = new_string + '\n'
        with open( 'dict.txt' , 'w', encoding = 'utf-8') as file:
            file.writelines(lines) 
            print(f"Строка {line_number} была успешно отредактирована.")
    else:
        print("Номер строки выходит за границы файла.")
def delete_line(surname):
    with open('Dict.txt', 'r', encoding = 'utf-8') as file:
        lines = file.readlines()

    with open('Dict.txt', 'w', encoding = 'utf-8') as file:
        for line in lines:
            if surname not in line:
                file.write(line)

  
   