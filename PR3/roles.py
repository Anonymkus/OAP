import os
from time import sleep
import shop
from pprint import pprint
from functools import reduce
from abc import ABC, abstractmethod


class Role(ABC):
    def __init__(self, role, name, phone, password, date):
        self.role = role
        self.name = name
        self.phone = phone
        self.password = password
        self.creations_date = date
    
    @abstractmethod
    def view_profile():
        pass


class Guest(Role):
    def __init__(self, role: str, name: str, phone: str, password: str, 
                 date: str, cart: list, history: list, spent: int):
        super().__init__(role, name, phone, password, date)
        self.cart = cart
        self.history = history
        self.spent = spent

    def self_print(self):
        return f"{self.name} - {self.role}. Номер телефона: {self.phone}. Здесь с {self.creations_date}."

    def __view_history(self, merchandise):
        while True:
            os.system("cls")
            merch_id = 0
            if len(self.history) == 0:
                print("История покупок пуста")
                sleep(1.5)
                return self
            for i in self.history:
                merch_id += 1
                print(merch_id, ": ", i)
            print("")
            print("Что дальше?")
            print(f"1 - Оценить\n0 - Назад")
            choice = input()
            print("")

            match choice:
                case "1":
                    while True:
                        os.system("cls")
                        try:
                            merch_id = int(input("Введите индекс товара, которого вы хотите оценить: "))
                            rate = float(input("Введите оценку от 0.0 до 10.0: "))
                        except Exception:
                            print("Вы должны ввести число!")
                            sleep(0.5)
                            continue
                        else:
                            if rate >= 0 and rate <= 10:
                                for i in merchandise:
                                    if i.title == self.history[merch_id-1]:
                                        i.rating = round((i.rating * (i.solled-1) + rate)/i.solled, 1)
                                print("Оценка поставлена")
                                sleep(0.5)
                                return self, merchandise
                            else:
                                print("Вы должны ввести число от 0.0 до 10.0")
                                continue
                case "0":
                    print("Возвращаемся...")
                    sleep(0.5)
                    return self, merchandise
                case _:
                    print("Такого действия нет")
                    sleep(0.5)
                    continue
        
            return self, merchandise
    
    def __view_cart(self, merchandise):
        while True:
            os.system("cls")
            merch_id = 1
            for i in self.cart:
                print(merch_id, ": ", i)
                merch_id+= 1
            print("Что дальше?")
            print(f"1 - Оплатить товары\n2 - Удалить товары\n0 - Назад")
            choice = input()
            print("")

            match choice:
                case "1":
                    while True:
                        os.system("cls")
                        if self.cart == []:
                            print("Ваша корзина пуста")
                            sleep(1.5)
                            break
                        print("")
                        j = 0
                        for i in self.cart:
                            j += 1
                            print(f"{j}: {i}")
                        print("")
                        try:
                            choice = int(input("Введите индекс товара или 0 для оплаты всей корзины: "))
                        except Exception:
                            print("Товара с таким индексом нет")
                            sleep(0.5)
                            continue
                        else:
                            if choice == 0:
                                for i in merchandise:
                                    for j in self.cart:
                                        if i.title == j:
                                            i.solled += 1
                                            self.spent += i.price 
                                for i in range(len(self.cart)):
                                    self.history.append(self.cart[i])
                                self.cart.clear()
                                print("Все товары оплачены")
                                sleep(0.5)
                                break     
                            else:
                                if choice <= len(self.cart):
                                    for i in merchandise:
                                        if i.title == self.cart[choice-1]:
                                            i.solled += 1
                                            self.spent += i.price
                                    self.history.append(self.cart[choice-1])
                                    self.cart.pop(choice-1)
                                    print("Товар оплачен")
                                    sleep(0.5)
                                    break
                                else:
                                    print("Товара с таким индексом нет")
                                    sleep(0.5)
                                    continue
                case "2":
                    while True:
                        print("")
                        for i in self.cart:
                            for j in range(len(self.cart)):
                                print(f"{j}: {i}")
                        print("")
                        try:
                            choice = int(input("Введите индекс товара или 0 для удаления всей корзины: "))
                        except Exception:
                            print("Товара с таким индексом нет")
                            sleep(0.5)
                        else:
                            if choice == 0:
                                self.cart.clear()
                                print("Все товары удалены")
                            else:
                                if choice < len(self.cart):
                                    self.cart.pop(choice-1)
                                    print("Товар удален")
                                else:
                                    print("Товара с таким индексом нет")
                                    sleep(0.5)
                                    continue
                case "0":
                    print("Возвращаемся...")
                    sleep(0.5)
                    return self, merchandise
                case _:
                    print("Такого действия нет")
                    sleep(0.5)
                    continue
            
            return self, merchandise
            
    def __change(self, mode: int):
        while True:
            os.system("cls")
            if mode:
                old_pw = input("Введите текущий пароль: ")
                new_pw = input("Введите новый пароль: ")
                new2_pw = input("Повторите новый пароль: ")
                if old_pw != self.password:
                    print("Это не ваш пароль")
                    sleep(0.5)
                    continue
                else:
                    if new2_pw != new_pw:
                        print("Пароли не совпадают")
                        continue
                    else:
                        print("Ваш пароль изменен")
                        sleep(0.5)
                        self.password = new_pw
                        return self
            else:
                new_pn = input("Введите новый номер телефона: ")
                print("Ваш номер телефона изменен")
                sleep(0.5)
                self.phone_number = new_pn
                return self

    def view_profile(self, merchandise):
        while True:
            os.system("cls")
            print(f"Привет, {self.role} {self.name}.\n Ты здесь с {self.creations_date} и за это время потратил {self.spent}.")
            print("")
            print("Чего хочешь?")
            print(f"1 - Посмотреть историю покупок\n2 - Посмотреть корзину\n3 - Изменить пароль\n4 - Изменить номер телефона\n5 - Назад")
            choice = input()
            print("")

            match choice:
                case "1":
                    self, merchandise = self.__view_history(merchandise)
                case "2":
                    self, merchandise = self.__view_cart(merchandise)
                case "3":
                    self = self.__change(1)
                case "4":
                    self = self.__change(0)
                case "0":
                    print("Возвращаемся...")
                    sleep(0.5)
                    return self
                case _:
                    print("Такого действия нет")
                    sleep(0.5)
                    continue
            return self, merchandise

class Admin(Role):
    def __init__(self, role: str, name: str, phone: str, password: str, date: str):
        super().__init__(role, name, phone, password, date)

    def self_print(self):
        return f"{self.name} - {self.role}. Номер телефона: {self.phone}. Здесь с {self.creations_date}."

    def view_profile(self, logins):
        os.system("cls")
        for i, j in logins.items():
            if j.role == "админ":
                print(f"{i} - {j.role}. Номер телефона - {j.phone}. Здесь с {j.creations_date}")
            else:
                print(f"{i} - {j.role}. Номер телефона - {j.phone}. Здесь с {j.creations_date}. Потрачено {j.spent}")
        print("")
        input("Нажмите Enter, чтобы продолжить ")
        return
    
    def view_stats(self, logins, merchandise):
        os.system("cls")
        solled = {}
        rated = {}
        spent = {}
        total_spent = []
        for i in merchandise:
            solled[i.solled] = f"{i.title} - {i.solled}"
            rated[i.rating] = f"{i.title} - {i.rating}"
            total_spent.append(i.price*i.solled)
        for i, j in logins.items():
            if j.role == "посетитель":
                spent[j.spent] = f"{j.name} - {j.spent}"

        print(f"Самый продаваемый товар: {solled[max(solled)]}")
        print(f"Наименее продаваемый товар: {solled[min(solled)]}")
        print("")
        print(f"Самый высокооцененный товар: {rated[max(rated)]}")
        print(f"Самый низкооцененный товар: {rated[min(rated)]}")
        print("")
        print(f"Наибольшая сумма, потраченная клиентом: {spent[max(spent)]}")
        print(f"Наименьшая сумма, потраченная клиентом: {spent[min(spent)]}")
        print("")
        print(f"Потрачено клиентами всего: {reduce(lambda x, y: x+y, total_spent)}")
        input(("Нажмите Enter, чтобы продолжить "))
        return
