from time import sleep, time
from threading import Thread
import os
import datetime as dt
from saveload import save_data, load_data

file_path = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")


def auto_save(users, ids):
    while True:
        sleep(10)
        save_data(users, ids)


if os.path.exists("data.txt"):
    users, ids = load_data()
else:
    users = {
        "admin" : "admin",
    }

    ids = {
        "admin" : 0,
    }

saving_thread = Thread(target=auto_save, args=(users, ids), daemon=True)
saving_thread.start()


def auth():
    os.system("cls")
    login = input("Введите логин: ")
    passwd = input("Введите пароль: ")
    
    for i, j in users.items():
        if login == i and passwd == j:
            sleep(0.5)
            return login
    
    print("Ошибка в логине или пароле!")
    sleep(0.7)


def reg():
    global license
    os.system("cls")
    login = input("Введите логин: ")
    passwd = input("Введите пароль: ")
    passwd2 = input("Повторите пароль: ")

    if login not in users.keys():
        if passwd == passwd2:
            print(f"Пользователь {login} зарегистрирован")
            users[login] = passwd
            ids[login] = 0
            sleep(0.7)
            return login
        else:
            print("Пароли не совпадают")
    else:
        print("Этот логин занят")
    sleep(0.7)


def view_note(login: str):
    os.system("cls")
    with open(f"notes/{login}_notes.txt", "r", encoding='utf8') as note:
        for line in note:
            print(line)
    print("")


def add_note(login: str, mode: bool):
    while True:
        os.system("cls")
        food = input(f"{"Введите пищу: " if mode else "{}"}")
        if food == "":
            print("Введите пищу")
            sleep(0.7)
            continue

        date = input("Введите дату приема пищи (дд.мм.гггг): ").split(".")
        try:
            dt.date(int(date[2]), int(date[1]), int(date[0]))
            date = [date[2], date[1], date[0]]
        except:
            print("Дата введена в неправильном формате")
            sleep(0.7)
            continue

        time = input("Введите время приема пищи (чч:мм в 24-часовом формате): ").split(":")
        try:
            dt.time(int(time[0]), int(time[1]))
            time = [time[0], time[1]]
        except:
            print("Время введено в неправильном формате")
            sleep(0.7)
            continue

        kcal = input("Введите калорийность пищи: ")
        try:
            kcal = float(kcal)
            0 / (kcal + abs(kcal))
        except:
            print("Ккал - число не меньше 0")
            sleep(0.7)
            continue

        pfc = input("Введите БЖУ пищи (Жиры/Белки/Углеводы): ").split("/")
        try:
            float(pfc[0])
            float(pfc[1])
            float(pfc[2])
        except:
            print("БЖУ записано в неправильном формате")
            sleep(0.7)
            continue

        ids[login] += 1
        break
    with open(f"notes/{login}_notes.txt", "a", encoding='utf8') as note:
        note.write(f"{ids[login]}|Пища: {food}|Время: {date[2]}.{date[1]}.{date[0]} {time[0]}:{time[1]}|Ккал: {kcal}|БЖУ: {pfc[0]}/{pfc[1]}/{pfc[2]}|" + "\n")
    return


def del_note(login: str):
    while True:
        os.system("cls")
        view_note(login)
        id = input("Введите индекс записи, которую вы хотите удалить: ")
        os.rename(f"{file_path}/notes/{login}_notes.txt", f"{file_path}/notes/old_file.txt")
        old_file = open("notes/old_file.txt", "r", encoding='utf8') 
        with open(f"notes/{login}_notes.txt", "a", encoding='utf8') as note:
            for line in old_file:
                del_id = line[:line.find('|')]
                print(del_id)
                if del_id != id:
                    note.write(line + "\n")
        old_file.close()
        os.remove(f"{file_path}/notes/old_file.txt")
        return


    