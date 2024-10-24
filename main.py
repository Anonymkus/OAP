import os 
import os.path
import random


def cheat_code(u_stat):
    card_num = ""
    card_date = ""
    card_cvv = ""
    print(f"{u_stat["Имя"]} решило, что эта игра - пустая трата времнени,")
    print("что является чистой правдой. Поэтому силой сюжета оно смогло открыть консоль.")
    while len(card_num) != 16:
        card_num = input("Введите номер вашей банковской карты: ")
        if len(card_num) == 16:
            try:
                card_num = int(card_num)
                print(f"Молодец {u_stat["Имя"]}!")
                break
            except ValueError:
                print("Напиши номер карты цифрами без пробелов и других знаков!")
                card_num = ""
        else:
            print("Напиши номер карты цифрами без пробелов и других знаков!")
            card_num = ""
    while len(card_date) != 4:
        card_date = input("Введите дату вашей банковской карты: ")
        if len(card_date) == 4:
            try:
                card_date = int(card_date)
                print(f"Молодец {u_stat["Имя"]}!")
                break
            except ValueError:
                print("Напиши дату карты 4 цифрами без пробелов и других знаков!")
                card_date = ""
        else:
            print("Напиши дату карты 4 цифрами без пробелов и других знаков!")
            card_date = ""
    while len(card_cvv) != 3:
        card_cvv = input("Введите cvv вашей банковской карты: ")
        if len(card_cvv) == 3:
            try:
                card_cvv = int(card_cvv)
                print(f"Молодец {u_stat["Имя"]}!")
                break
            except ValueError:
                print("Напиши cvv карты 3 цифрами без пробелов и других знаков!")
                card_cvv = ""
        else:
            print("Напиши cvv карты 3 цифрами без пробелов и других знаков!")
            card_cvv = ""
    print("Поздравляю с совершением транз.. с победой в игре!")
    return False


def show_stat(u_stat):
	print(f"Имя: {u_stat['Имя']}")
	print(f"Бюджет: {u_stat['Бюджет']}")
	print(f"Здоровье: {u_stat['Здоровье']}")
	print(f"Сила: {u_stat['Сила']}")
	print(f"Удача: {u_stat['Удача']}")
	print(f"Инвентарь:")
	for item in u_stat['Инвентарь']:
		print(" •", item)
	print("")
     

def show_market_place(u_stat):
    is_busy = True
    potion_prise = 100
    while is_busy:
        os.system("cls")
        show_stat(u_stat)
        print(f"1 — Купить боярышник за {potion_prise}.")
        print("2 — Пойти выключить несуществующий утюг.")
        choice = input("Что делать? ")

        if choice == "1" and u_stat["Бюджет"] >= potion_prise:
            u_stat["Бюджет"] -= potion_prise
            u_stat["Инвентарь"].append("Боярышник")
            print(f"{u_stat["Имя"]} купило боярышник.")
        elif choice == "1" and u_stat["Бюджет"] < potion_prise:
            print(f"У {u_stat["Имя"]} маловато рупий.")
        elif choice == "2":
            is_busy = False
            print(f"{u_stat["Имя"]} решило не отдавать вещь и пошло в бан.")
        else:
            print("У меня ощущение, что ты что-то не догоняешь.")

        input("ENTER — дальше")


def show_location(u_stat):
    is_busy = True
    u_bet = 0
    u_score = 0
    while is_busy:
        os.system("cls")
        show_stat(u_stat)
        print("А вот и игральная - место, в котором проигрывают жизнь, зато закуски вкусные.")
        print("1 — Сыграть")
        print("2 — Уйти")
        choice = input("Что делать? ")

        if choice == "1":
            u_bet = int(input("Сколько поставишь на игру? "))
            if u_bet > u_stat["Бюджет"]:
                print(f'Прости {u_stat["Имя"]} я не могу предоставить тебе кредит. Возвращяйся когда ты станешь... М-м-м... побогаче')
            elif u_bet < 1 or type(u_bet) == str:
                print("Не судьба")
            else:
                u_score = random.randint(2, 12)
                dice_score = random.randint(2, 12)
                print(f"{u_stat["Имя"]} выбросило {u_score}")
                print(f"У оппонента {dice_score}")

                if u_score > dice_score:
                    u_stat["Бюджет"] += u_bet
                    print(f"{u_stat["Имя"]} выиграло {u_bet} деньго-штук.")
                elif u_score < dice_score:
                    u_stat["Бюджет"] -= u_bet
                    print(f"Неудачник {u_stat["Имя"]} проиграло {u_bet} деньго-штук.")
                else:
                    print("Ничья!")
        
        elif choice == "2":
            is_busy = False
            print(f"{u_stat["Имя"]} свалило куда подальше.")        
        else:
            print("Мне кажется ты что-то не поняло.")

        input("ENTER — дальше")


game = True
u_stat = {
    "Имя" : "",
    "Бюджет" : 500,
    "Здоровье" : 100,
    "Сила" : 10,
    "Инвентарь" : ["Поп ит"],
    "Удача" : 1
}

print("Добро пожаловать в игру про непонятно что на Python")
print("Чтобы у тебя было ощущение выбора хоть где-то, ")
print("напиши сам данные своего персонажа и не забудь нажать на ENTER")
u_stat["Имя"] = input("Выбери имя персонажа - ") 
print("Ты проснулось где-тo, а главное зачем-тo.")
print("И не само собой перед тобой 2 пути.")
print("По странной и непонятной причине ты знаешь куда они ведутЮ")
print("а также ты знаешь, что для победы тебе нужно купить 10 боярышников.")
input("ENTER - продолжить")


while game:    
    if u_stat["Бюджет"] < 1 or u_stat["Инвентарь"].count("Боярышник"):
        game = False
    else:
        os.system("cls")
        show_stat(u_stat)
        print("Ты на развилке...")
        print("1 — Лавка. Приготовьте свои рупии.")
        print("2 — Игра в кости. Время заработка, вопрос чего.")
        print("-1 — Путь для слабаков.")
        print("0 — Выйти из игры.")
        choice = int(input("Чего желаете? "))

        match choice:
            case 1:
                show_market_place(u_stat)
            case 2:
                show_location(u_stat)
            case 0:
                game = False
            case -1:
                game = cheat_code(u_stat)
            case _:
                print("Ощущение выбора, а не сам выбор.")
                input("ENTER — дальше")

print("Конец. Это самое худшая трата вашего времни, поздравляю")
