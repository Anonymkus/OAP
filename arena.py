# нереализованная функция

import os
import stats
from random import choice
from time import monotonic
t = monotonic()


def show_location(u_stat):
    is_busy = True
    while is_busy:
        os.system("cls")
        stats.show_stat(u_stat)
        print(f"{u_stat['Имя']} вошло на арену.")
        print("1 — Сразиться")
        print("2 — Свалить")
        user_choice = input("Что делать? ")
        if user_choice == "1":
            enemy_first_names = ["Поц", "Клоун", "Чертилла"]
            enemy_second_names = ["Необыкновенный", "Обыкновенный", "Очуменный"]
            enemy_name = choice(enemy_first_names) + " " + choice(enemy_second_names)
            enemy_hp = 100
            is_fighting = True
            while is_fighting:
                os.system("cls")
                stats.show_stat(u_stat)
                print(f"Погоняло соперника: {enemy_name}")
                print(f"Здоровья только: {enemy_hp}")
                print("GLHF")
                print("")
                print("1 - Атаковать")
                print("2 - Защищаться")
                if "Боярышник" in u_stat["Инвентарь"]:
                    print("3 - Выпить зелье здоровья")
                if monotonic() - t > 5:
                    t = monotonic()
                    print('долго думаешь')
                    u_stat['Здоровье'] -= 10
                    print(f"{u_stat['Имя']} поймало маслину, -10хп")
                else:
                    u_choice = input("Что делать? ")

                    if u_choice == "1":
                        enemy_hp -= 10
                        print(f"{enemy_name} получил -10хп в лицо")
                    elif u_choice == "2":
                        u_stat['Здоровье'] -= 5
                        print(f"{u_stat['Имя']} поймало маслину, -5хп")
                    elif u_choice == "3" and "зелье" in u_stat["Инвентарь"]:
                        print(f"{u_stat['Имя']} подвыпило и похилилось")
                        u_stat["Инвентарь"].remove("боярышник")
                        u_stat["Имя"] = 100
                    else:
                        print("Ты опять не догоняешь, и опять меня разачаровываешь.")

                    input("ENTER — продолжить")

        elif user_choice == "2":
            is_busy = False
            print(f"{u_stat['Имя']} свалило.")
        else:
            print(f"Давай по новой {u_stat['Имя']}, все плохо.")

        input("ENTER — дальше")
