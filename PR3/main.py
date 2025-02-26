import os
from time import sleep
import shop
from shop import Merch
from roles import Guest, Admin
from savenload import save_data, load_data

logins = dict()
merchandise = list()

if os.path.exists("data.txt"):
    logins, merchandise = load_data()
else:
    logins["ArtOfArms"] = Admin("админ", "Нико", "222", "45cal", "01.07.2018")
    logins["DeadWeight"] = Guest("посетитель", "Неро", "333", "kyrie","01.03.2019", ["Прелюдия", "Починка"], [], 6500)
    logins["admintest"] = Admin("админ", "ТестАдмина", "000", "qwe","21.02.2024")
    logins["usertest"] = Guest("посетитель", "ТестКлиента", "111", "qwe","21.02.2024", [], [], 0)
    merchandise.append(Merch(40, "Орб", "Синий орб", 500, 8.8, "24.07.2018", 5))
    merchandise.append(Merch(24, "Орб", "Фиолетовый орб", 1500, 10.0, "17.08.2018", 8))
    merchandise.append(Merch(84, "Оружие", "Red Quenn II", 20000, 0.0, "07.07.2019", 0))
    merchandise.append(Merch(19, "Оружие", "Kalina Ann II", 15000, 7.9, "14.06.2019", 1))
    merchandise.append(Merch(73, "Услуга", "Починка", 5000, 8.4, "13.08.2018", 21))
    merchandise.append(Merch(46, "Услуга", "Транспортировка", 3000, 2.4, "13.08.2018", 25))
    merchandise.append(Merch(94, "Бич Дьяволов", "Прелюдия", 1500, 9.2, "10.06.2019", 17))
    merchandise.append(Merch(68, "Бич Дьяволов", "Томбой", 3000, 6.9, "14.06.2019", 9))


is_shop = True

while is_shop:
    os.system("cls")
    print("Приветствую в магазинчике Нико!")
    print("")
    shopping = True

    if input("Введите 0, чтобы завершить работу или нажмите Enter, чтобы продолжить: ") == "0":
        print("Завершаем работу...")
        sleep(1.5)
        shopping = False
        is_shop = False
        break

    login = input("Введите логин или номер: ")
    password = input("Введите пароль: ")
    error = True

    for i, j in logins.items():
        if (login == i or login == j.phone) and password == j.password:
            user = logins[i]
            login = i
            error = False

    if error:
        print("Такого пользователя нет")
        sleep(1.5)
    else:
        while shopping:
            os.system("cls")
            if user.role == "посетитель":
                logins[login] = user
                save_data(logins, merchandise)
                logins, merchandise = load_data()
                print(f"Привет, {user.role} {user.name}")
                print("Чего вы хотите?")
                print(f"1 - Перейти к покупкам\n2 - Перейти к профилю\n0 - Разлогиниться")
                print("")
                choice = input()

                match choice:
                    case "1":
                        user, merchandise = shop.buy_merch(merchandise, user)
                    case "2":
                        user, merchandise = user.view_profile(merchandise)
                    case "0":
                        print("Разлогиниваемся...")
                        sleep(1.5)
                        shopping = False
                    case _:
                        print("Такого действия нет")
                        sleep(1.5)
            else:
                logins[login] = user
                save_data(logins, merchandise)
                logins, merchandise = load_data()
                print(f"Приветствую, {user.role} {user.name}")
                print("Чего вы хотите?")
                print(f"1 - Добавить данные\n2 - Изменить данные\n3 - Удалить данные\n4 - Посмотреть статистику\n5 - Посмотреть пользователей\n0 - Разлогинеться")
                print("")
                choice = input()
                match choice:
                    case "1":
                        merchandise, logins = shop.update_data(1, merchandise, logins)
                    case "2":
                        merchandise, logins = shop.update_data(2, merchandise, logins)
                    case "3":
                        merchandise, logins = shop.update_data(3, merchandise, logins)
                    case "4":
                        user.view_stats(logins, merchandise)
                    case "5":
                        user.view_profile(logins)
                    case "0":
                        print("До свидания")
                        sleep(1.5)
                        shopping = False
                        save_data(logins, merchandise)
                        break
                    case _:
                        print("Такого выбора пока нет")
                        sleep(1.5)