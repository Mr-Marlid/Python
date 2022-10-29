s = input("Введите имя файла: ")
s1 = ""
while s!="stop":
    try:
        f = open(s,'r')
        s1 += f.read()
    except FileNotFoundError:
        if s!="":
            print("Файл", s," не найден. Попробуйте еще.")
        else:
            print("Вы не ввели название файла...")
    s = input("Введите имя файла: ")
print(s1)