from threading import Thread
import funcs
import os
from time import sleep, time

file_path = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")


def license_check():
    global license
    start = float(time())
    while True:
        sleep(1)
        if float(time()) - start >= license:
            license = 0
            break
        

license_thread = Thread(target=license_check, daemon=True)

login = None
first_enter = False
while True:
    os.system("cls")
    if login == None:
        print("Дневник питания")
        print("")
        print("1 - Авторизация")
        print("2 - Регистрация")
        print("0 - Выход")
        choice = input("Введите вариант: ")

        match choice:
            case "1":
                login = funcs.auth()
                first_enter = True
            case "2":
                login = funcs.reg()
                first_enter = True
            case "0":
                print("Выход...")
                sleep(0.5)
                break
            case _:
                print("Такого варианта нет!")
                sleep(0.7)

    else:
        if first_enter:
            if os.path.exists(f"{file_path}/licenses/{login}_license.txt"):
                license = open(f"licenses/{login}_license.txt", "r")
                license = float(license.read()) * 60
                if license != 0.0:
                    print(f"Лицензия подтверждена, время вашего доступа в минутах равно: {license/60}")
                    sleep(2)
                    license_thread.start()
            else:
                print("Лицензия не подтверждена")
                sleep(2)
                login = None
                continue
            first_enter = False
        if license == 0:
            print("Действие лицензии завершено")
            license = open(f"licenses/{login}_license.txt", "w")
            license.write("0")
            sleep(2)
            break
        os.system("cls")
        print(f"Здраствуйте, {login}")
        print("")
        print("1 - Просмотр записи")
        print("2 - Добавление записи")
        print("3 - Удаление записи")
        print("0 - Выход")
        choice = input("Введите вариант: ")

        match choice:
            case "1":
                funcs.view_note(login)
            case "2":
                funcs.add_note(login, True)
            case "3":
                funcs.del_note(login)
            case "0":
                print("Выход...")
                sleep(0.5)
                break
            case _:
                print("Такого варианта нет!")
                sleep(0.7)

        input("Нажмите Enter, чтобы продолжить...")            
