import os
import sys
import datetime
import roles
from time import sleep

def pretty_print(el):
    for i in el:
        print(f"\n{i.id}: {i.title} ({i.type}) - price: {i.price}, rating: {i.rating}, date added: {i.date}. Solled: {i.solled}")


class Merch:
    def __init__(self, id: int, type: str, title: str, 
                 price: int, rating: float, date: str, solled: int):
        self.id = id
        self.type = type
        self.title = title
        self.price = price
        self.rating = rating
        self.date = date
        self.solled = solled


def update_merch(mode, merchandise):
    while True:
        os.system("cls")
        match mode:
            case 1:
                new_type = input("Введите тип нового товара: ").capitalize().strip()
                new_title = input("Введите название нового товара: ").capitalize().strip()
                new_price = input("Введите цену новго товара: ").strip()
                date = datetime.datetime.now().strftime('%d.%m.%Y')
                try:
                    new_price = int(new_price)
                except Exception:
                    print("Цена должна быть числом")
                    sleep(1.5)
                    continue
                else:
                    merch_id = []
                    for i in merchandise:
                        if i.title == new_title:
                            print()
                        merch_id.append(i.id)
                    merch_id = max(merch_id)+1
                    
                    merchandise.append(Merch(merch_id, new_type, new_title, new_price, 0.0, date, 0))
                    print("")
                    print("Товар добавлен")
                    sleep(1.5)
                return merchandise
            case 2:
                print(*list(map(lambda merch: f"\n{merch.id}: {merch.title} ({merch.type}) - price: {merch.price}, rating: {merch.rating}, date added: {merch.date}. Solled: {merch.solled}", merchandise)))
                print("")
                upd_merch = input("Введите индекс товара, которого вы хотите изменить: ")

                for i in merchandise:
                    if upd_merch == str(i.id):
                        upd_merch = merchandise.index(i)
                if type(upd_merch) == str:
                    print("Товара с таким индексом нет")
                    sleep(1.5)
                    continue
                else:
                    upd_type = input("Введите новый тип или оставьте поле пустым: ")
                    upd_title = input("Введите новое название или оставьте поле пустым: ")
                    upd_price = input("Введите новую цену или оставьте поле пустым: ")

                    if upd_price.isdigit() or upd_price == "":
                        if upd_type != "":
                            merchandise[upd_merch].type = upd_type
                        if upd_title != "":
                            merchandise[upd_merch].title = upd_title
                        if upd_price != "":
                            merchandise[upd_merch].price = abs(int(upd_price))
                        print("Товар изменен")
                        sleep(1.5)
                    else:
                        print("Цена должна быть числом или быть пропущена")
                        sleep(1.5)
                        continue
                return merchandise
            case 3:
                print(*list(map(lambda merch: f"\n{merch.id}: {merch.title} ({merch.type}) - price: {merch.price}, rating: {merch.rating}, date added: {merch.date}. Solled: {merch.solled}", merchandise)))
                print("")
                del_merch = input("Введите индекс товара, которого вы хотите удалить: ")
                ids_merch = []
                for i in merchandise:
                    ids_merch.append(str(i.id))
                    merch_id = merchandise.index(i)

                if del_merch not in ids_merch:
                    print("Введенный индекс отсутствует в списке, повторите попытку")
                    sleep(1.5)
                    continue
                else:
                    merchandise.pop(merch_id)
                    print("Товар удален")
                    sleep(1.5)
                return merchandise
        return merchandise


def update_user(mode: str, logins: dict):
    while True:
        os.system("cls")
        match mode:
            case 1:
                new_role = input("Введите роль (посетитель или админ): ").lower()
                new_login = input("Введите логин нового пользователя: ")
                new_name = input("Введите имя нового пользователя: ")
                new_phone = input("Введите номер телефона нового пользователя: ")
                new_passwd = input("Введите пароль нового пользователя: ")
                creations_date = datetime.datetime.now().strftime('%d.%m.%Y')

                for i, j in logins.items():
                    if new_login == i:
                        print("Введенный логин уже используется, повторите попытку")
                        sleep(1.5)
                        continue
                    if new_phone == j.phone:
                        print("Введенный номер телефона уже используется, повторите попытку")
                        sleep(1.5)
                        continue
                
                if new_role == "посетитель":
                    logins[new_login] = roles.Guest(new_role, new_name, new_phone, 
                    new_passwd, creations_date, [], [], 0)
                    print(f"Новый {new_role} создан")
                elif new_role == "админ":
                    logins[new_login] = roles.Admin(new_role, new_name, new_phone, 
                    new_passwd, creations_date)
                    print(f"Новый {new_role} создан")
                else:
                    print("Введенной роли не существует, повторите попытку")
                    sleep(1.5)
                    continue
                sleep(1.5)
                return logins
            case 2:
                os.system("cls")
                for i, j in logins.items():
                    print(f"{i}. {j.self_print()}")
                    
                upd_login = input("Введите логин пользователя, которого вы хотите изменить: ")
                if upd_login not in logins.keys():
                    print("Введынный логин отсутствует в списке, повторите попытку")
                    sleep(1.5)
                    continue
                else:
                    upd_name = input("Введите новое имя или оставьте поле пустым: ")
                    upd_phone = input("Введите новый номер телефона или оставьте поле пустым: ")
                    upd_passwd = input("Введите новый пароль или оставьте поле пустым: ")

                    if upd_name != "":
                        logins[upd_login].name = upd_name
                    if upd_phone != "":
                        logins[upd_login].phone = upd_phone
                    if upd_passwd != "":
                        logins[upd_login].passwd = upd_passwd

                    print("Пользователь изменен")
                    sleep(1.5)
                return logins
            case 3:
                os.system("cls")
                for i, j in logins.items():
                    print(f"{i}. {j.self_print()}")
                    
                del_login = input("Введите логин пользователя, которого вы хотите изменить: ")
                if del_login not in logins.keys():
                    print("Введынный логин отсутствует в списке, повторите попытку")
                    sleep(1.5)
                    continue
                else:
                    logins.pop(del_login)
                    print("Пользователь удален")
                    sleep(1.5)
                return logins
        return logins


def update_data(mode: str, merchandise: dict, logins: dict):
    while True:
        os.system("cls")
        print("Выберите с чем будете работать")
        print(f"1 - Пользователи\n2 - Товары\n0 - Назад")
        print("")

        choice = input()

        match choice:
            case "1":
                logins = update_user(mode, logins)
            case "2":
                merchandise = update_merch(mode, merchandise)
            case "0":
                print("Возвращаемся...")
                sleep(1.5)
            case _:
                print("Такого действия нет")
                sleep(1.5)
                continue

        return merchandise, logins


def search_merch(merchandise, user):
    while True:
        os.system("cls")
        print("Введите название или его часть:")
        find_merch = input()
        merch = list()
        searched_merch = list()
        for i in merchandise:
            merch.append(i.title)
        
        for i in merch:
            if find_merch.lower() in i.lower():
                searched_merch.append(merchandise[merch.index(i)])
        if searched_merch != []:
            while(True):
                os.system("cls")
                print(*list(map(lambda merch: f"\n{merch.id}: {merch.title} ({merch.type}) - цена: {merch.price}, рейтинг: {merch.rating}, дата добавления: {merch.date}. Продано: {merch.solled}", searched_merch)))
                print("")
                print("1 - Купить товар")
                print("0 - Назад")
                choice = input("Что дальше? ")

                match choice:
                    case "1":
                        merch_id = input("Введите индекс товара: ")
                        for i in searched_merch:
                            if str(i.id) == merch_id:
                                user.cart.append(merchandise[merchandise.index(i)].title)
                                print(f"Вы купили {i.title}")
                                sleep(1.5)
                                break
                    case "0":
                        print("Возвращаемся...")
                        sleep(1.5)
                        break
                    case _:
                        print("Такого действия нет")
                        sleep(1.5)
                        continue
        else:
            print("Ничего не найдено")
            sleep(1.5)
            continue
        return user
    

def filter_merch(merchandise, user):
    all_types = set()
    for i in merchandise:
        all_types.add(i.type)
    all_types = list(all_types)
    while True:
        os.system("cls")
        print("Сортировка по ")
        print(f"1 - Возрастанию цены\n2 - Убыванию цены\n3 - Рейтингу\n4 - Популярности\n0 - Дефолту")
        merch_sort = input("Выберите тип сортировки: ")
        if merch_sort != "0" and merch_sort != "1" and merch_sort != "2" and merch_sort != "3" and merch_sort != "4":
            print("Такого типа сортировки нет")
            sleep(1.5)
            continue
        merch_sort = int(merch_sort)
        print("Типы товаров")
        num = 0
        for i in all_types:
            num+=1
            print(f"{num} - {all_types[num-1]}")
        print(f"0 - Все типы")
        merch_type = input("Выберите тип товара: ")
        if not(merch_type.isdigit()) or (merch_type.isdigit() and (int(merch_type) < 0 and int(merch_type) > num)):
            print("Такого типа товаров нет")
            sleep(1.5)
            continue
        if int(merch_type) != 0:
            merch_type = [all_types[int(merch_type)-1]]
        else:
            merch_type = all_types
        min_price = input("Введите минимальную цену или пропустите ввод: ")
        max_price = input("Введите максимальную цену или пропустите ввод: ")
        if min_price != "" and not(min_price.isdigit) and max_price != "" and not(max_price.isdigit):
            print("Цена должна быть числом или пустой")
            sleep(1.5)
            continue
        if max_price == "":
            max_price = sys.maxsize
        if min_price == "":
            min_price = 0

        min_rating = input("Введите минимальный рейтинг или пропустите ввод: ")
        max_rating = input("Введите максимальный рейтинг или пропустите ввод: ")
        if min_rating != "" and not(min_rating.isdigit) and max_rating != "" and not(max_rating.isdigit):
            print("Рейтинг должен быть числом или пустым")
            sleep(1.5)
            continue
        if max_rating == "":
            max_rating = 10.0
        if min_rating == "":
            min_rating = 0.0
        
        min_price = int(min_price)
        max_price = int(max_price)
        min_rating = int(min_rating)
        max_rating = int(max_rating)
        while True:
            os.system("cls")
            match merch_sort:
                case 0:
                    pretty_print(list(filter(lambda merch: merch.type in merch_type and merch.price > min_price and merch.price < max_price and merch.rating > min_rating, merchandise), key=lambda merch: merch.price))
                case 1:
                    pretty_print(list(sorted(filter(lambda merch: merch.type in merch_type and merch.price > min_price and merch.price < max_price and merch.rating > min_rating, merchandise), key=lambda merch: merch.price)))
                case 2:
                    pretty_print(list(sorted(filter(lambda merch: merch.type in merch_type and merch.price > min_price and merch.price < max_price and merch.rating > min_rating, merchandise), key=lambda merch: merch.price, reverse=True)))
                case 3:
                    pretty_print(list(sorted(filter(lambda merch: merch.type in merch_type and merch.price > min_price and merch.price < max_price and merch.rating > min_rating, merchandise), key=lambda merch: merch.rating)))
                case 4:
                    pretty_print(list(sorted(filter(lambda merch: merch.type in merch_type and merch.price > min_price and merch.price < max_price and merch.rating > min_rating, merchandise), key=lambda merch: merch.solled, reverse=True)))
        
            print("")
            print("1 - Купить товар")
            print("0 - Назад")
            choice = input("Что дальше? ")

            match choice:
                case "1":
                    merch_id = input("Введите индекс товара: ")
                    for i in merchandise:
                        if str(i.id) == merch_id:
                            user.cart.append(merchandise[merchandise.index(i)].title)
                            print(f"Вы купили {i.title}")
                            sleep(1.5)
                            break
                case "0":
                    print("Возвращаемся...")
                    sleep(1.5)
                    break
                case _:
                    print("Такого действия нет")
                    sleep(1.5)
                    continue
        return user, merchandise


def buy_merch(merchandise, user):
    while True:
        os.system("cls")
        print(*list(map(lambda merch: f"\n{merch.id}: {merch.title} ({merch.type}) - цена: {merch.price}, рейтинг: {merch.rating}, дата добавления: {merch.date}. Продано: {merch.solled}", merchandise)))
        print("")
        print("Что дальше?")
        print("1 - Купить товар\n2 - Поиск товаров\n3 - Фильтры\n0 - Назад")
        choice = input()
        print("")

        match choice:
            case "1":
                merch_id = input("Введите индекс товара: ")
                for i in merchandise:
                    if str(i.id) == merch_id:
                        user.cart.append(merchandise[merchandise.index(i)].title)
                        print(f"Вы купили {i.title}")
                        sleep(1.5)
                        break
            case "2":
                user = search_merch(merchandise, user)
            case "3":
                user, merchandise = filter_merch(merchandise, user)
            case "0":
                print("Возвращаемся...")
                sleep(1.5)
                break
            case _:
                print("Такого действия нет")
                sleep(1.5)
                continue
    return user, merchandise

            
