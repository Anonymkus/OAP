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


def show_arena_location(u_stat):
    is_busy = True
    while is_busy:
        os.system("cls")
        show_stat(u_stat)
        print(f"{u_stat['Имя']} вошло на арену.")
        print("1 — Сразиться")
        print("2 — Свалить")
        user_choice = input("Что делать? ")
        if user_choice == "1":
            enemy_first_names = ["Поц", "Клоун", "Чертилла"]
            enemy_second_names = ["Необыкновенный", "Обыкновенный", "Очуменный"]
            enemy_name = f"{enemy_first_names[random.randint(0, 2)]} {enemy_second_names[random.randint(0, 2)]}"
            enemy_hp_t = random.randint(100, 201)
            enemy_hp = enemy_hp_t
            enemy_heals = random.randint(0, 1)
            is_fighting = True
            while is_fighting:
                if enemy_hp <= 0:
                    print(f"{u_stat["Имя"]} победило и зафармило сколько-то деньго-штук и абонемент в бассейн!")
                    u_stat["Бюджет"] += random.randint(50, 100)
                    u_stat["Инвентарь"].append("Абонемент")
                    break
                elif u_stat["Здоровье"] <= 0:
                    print(f"{u_stat["Имя"]} - неудачник, пока пока!")
                    return
                else:
                    os.system("cls")
                    show_stat(u_stat)
                    print(f"Погоняло соперника: {enemy_name}")
                    print(f"Здоровья только: {enemy_hp}")
                    print(f"Бояурышника у него: {enemy_heals}")
                    print("GLHF")
                    print("")
                    print("1 - Атаковать")
                    print("2 - Защищаться")
                    if "Боярышник" in u_stat["Инвентарь"]:
                        print("3 - Выпить зелье здоровья")
                    u_choice = int(input("Что делать? "))
                    u_attack = 0
                    e_block = 0
                    enemy_choice = random.randint(1, 2)

                    match u_choice:
                        case 1:
                            print(f"{u_stat['Имя']} атакует")
                            u_attack += 1
                        case 2:
                            print(f"{u_stat['Имя']} ставит блок")
                        case 3:
                            print(f"{u_stat['Имя']} подвыпило и похилилось")
                            u_stat["Инвентарь"].remove("боярышник")
                            u_stat["Имя"] = 100
                        case _:
                            print("Ты опять не догоняешь, и опять меня разачаровываешь.")
                    
                    if enemy_hp < enemy_hp_t/4 and enemy_heals != 0:
                        print(f"{enemy_name} подвыпил и похилился")
                        enemy_heals -= 1
                        enemy_hp = enemy_hp_t
                    else:
                        match enemy_choice:
                            case 1:
                                print(f"{enemy_name} атакует")
                            case 2:
                                print(f"{enemy_name} ставит блок")
                                e_block += 1
                            case _:
                                print("Ты опять не догоняешь, и опять меня разачаровываешь.")
                    if u_attack == 1:
                        if e_block:
                            enemy_hp -= 10
                            print(f"{u_stat["Имя"]} атаковало блокирующегося противника и снесло ему 10хп")
                        else:
                            enemy_hp -= 15
                            u_stat["Здоровье"] -= 10
                            print(f"{u_stat["Имя"]} атаковала атакующего противника: {enemy_name} получил маслину на 15хп,")
                            print(f"{u_stat["Имя"]} получил маслину на 10хп")
                    else:
                        if e_block:
                            print(f"{u_stat["Имя"]} и {enemy_name} заблокировали друг друга... зачем-то")
                        else:
                            u_stat["Здоровье"] -= 5
                            print(f"{u_stat["Имя"]} поставил блок и получил маслину в 5хп")

                input("ENTER — продолжить")

        elif user_choice == "2":
            is_busy = False
            print(f"{u_stat['Имя']} свалило.")
        else:
            print(f"Давай по новой {u_stat['Имя']}, все плохо.")

        input("ENTER — дальше")
    return


def show_stat(u_stat):
	print(f"Имя: {u_stat['Имя']}")
	print(f"Бюджет: {u_stat['Бюджет']}")
	print(f"Здоровье: {u_stat['Здоровье']}")
	print(f"Сила: {u_stat['Сила']}")
	print(f"Инвентарь:")
	for item in u_stat['Инвентарь']:
		print(" •", item)
	print("")
     

def show_market_place(u_stat):
    is_busy = True
    while is_busy:
        os.system("cls")
        show_stat(u_stat)
        print("1 — Купить боярышник за сотку.")
        print("2 — Купить абонемент в бассейн за двестипятьдесят.")
        print("3 — Пойти выключить несуществующий утюг.")
        choice = input("Что делать? ")
        match choice:
            case "1":
                if u_stat["Бюджет"] >= 100:
                    u_stat["Бюджет"] -= 100
                    u_stat["Инвентарь"].append("Боярышник")
                    print(f"{u_stat["Имя"]} купило боярышник.")
                elif u_stat["Бюджет"] < 100:
                    print(f"У {u_stat["Имя"]} маловато рупий.")
            case "2":
                if u_stat["Бюджет"] >= 250:
                    u_stat["Бюджет"] -= 250
                    u_stat["Инвентарь"].append("Абонемент")
                    print(f"{u_stat["Имя"]} купило абонемент в бассейн.")
                elif u_stat["Бюджет"] < 250:
                    print(f"У {u_stat["Имя"]} маловато рупий.")
            case "3":
                is_busy = False
                print(f"{u_stat["Имя"]} решило не отдавать вещь и пошло в бан.")
            case _:
                print("У меня ощущение, что ты что-то не догоняешь.")

        input("ENTER — дальше")
    return


def show_dice_location(u_stat):
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
    return


game = True
u_stat = {
    "Имя" : "",
    "Бюджет" : 2500,
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
print("а также ты знаешь, что для победы тебе нужно купить 10 абонементов в бассейн.")
input("ENTER - продолжить")


while game:    
    if u_stat["Инвентарь"].count("Абонемент") == 10:
        print("Ты отправляешься отдыхать в бассейн, молодец!")
        game = False
    elif u_stat["Здоровье"] <= 0:
        game = False
    else:
        os.system("cls")
        show_stat(u_stat)
        print("Ты на развилке...")
        print("1 — Лавка. Приготовьте свои рупии.")
        print("2 — Игра в кости. Время заработка, вопрос чего.")
        print("3 — Арена. Можно что-нибудь да выбить с кого-нибудь, а может и себя угробить.")
        print("-1 — Путь для слабаков.")
        print("0 — Выйти из игры.")
        choice = int(input("Чего желаете? "))

        match choice:
            case 1:
                show_market_place(u_stat)
            case 2:
                show_dice_location(u_stat)
            case 3:
                show_arena_location(u_stat)
            case 0:
                game = False
            case -1:
                game = cheat_code(u_stat)
            case _:
                print("Ощущение выбора, а не сам выбор.")
                input("ENTER — дальше")
    
print("Конец. Это самое худшая трата вашего времни, поздравляю")
