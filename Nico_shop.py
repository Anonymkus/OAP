import os
import datetime
from functools import reduce
from time import sleep

def pretty_print(el):
    for i in el:
        print(f"\n{i["id"]}: {i["title"]} ({i["type"]}) - price: {i["price"]}, rating: {i["rating"]}, date added: {i["date"]}. Solled: {i["solled"]}")

def buy(user):
    while True:
        os.system("cls")
        print(*list(map(lambda merch: f"\n{merch["id"]}: {merch["title"]} ({merch["type"]}) - price: {merch["price"]}, rating: {merch["rating"]}, date added: {merch["date"]}. Solled: {merch["solled"]}", merchandise)))
        print("_____________________________________")
        print("1 - buy smth")
        print("0 - get the Hell out")
        choice = input("Whatcha want? ")
        print("")

        match choice:
            case "1":
                try:
                    merch = int(input("Write the merch ID: "))
                except Exception:
                    print("There is no such merch")
                    sleep(0.5)
                else:
                    for i in merchandise:
                        if i["id"] == merch:
                            user["cart"].append(i["title"])
                            print(f"You buyed {i['title']}")
                    sleep(0.5)

            case "0":
                print("byeeeee")
                sleep(0.5)
                break
            case _:
                print("There is no such choice")
                sleep(0.5)

    return user


def search(user):
    os.system("cls")
    print("Find:")
    find_merch = input()
    merch = list()
    searched_merch = list()
    for i in merchandise:
        merch.append(i["title"])
    
    for i in merch:
        if find_merch.lower() in i.lower():
            searched_merch.append(merchandise[merch.index(i)])
    if searched_merch != []:
        while(True):
            os.system("cls")
            pretty_print(searched_merch)
            print("_____________________________________")
            print("1 - buy smth")
            print("0 - get the Hell out")
            choice = input("Whatcha want? ")

            match choice:
                case "1":
                    try:
                        print("")
                        merch = int(input("Write the merch ID: "))
                    except Exception:
                        print("There is no such merch")
                        sleep(0.5)
                    else:
                        for i in merchandise:
                            if i["id"] == merch:
                                user["cart"].append(i["title"])
                case "0":
                    print("byeeeee")
                    sleep(0.5)
                    break
                case _:
                    print("There is no such choice")
                    sleep(0.5)
    else:
        print("Nothing found")
        sleep(0.5)
    return user


def sortnfilter(user):
    while True:
        os.system("cls")
        print("Sorted by")
        print("1 - Ascending price")
        print("2 - Decending price")
        print("3 - Rating")
        print("4 - Popularity")
        print("0 - Deafult")
        merch_sort = input("Whatcha want? ")
        try:
            merch_sort = int(merch_sort)
            if merch_sort < 0 and merch_sort > 4:
                print("There is no such sort")
                sleep(0.5)
                merch_sort = 0
        except Exception:
            print("There is no such sort")
            sleep(0.5)
        else:
            os.system("cls")
            print("Types:")
            print("1 - Devil Breaker")
            print("2 - Orb")
            print("3 - Weapon")
            print("4 - Service")
            print("0 - All")
            merch_types = {1: "Devil Breaker", 2: "Orb", 3: "Weapon", 4: "Service"}
            merch_type = input("Enter type or pass this: ")
            try:
                merch_type = int(merch_type)
                if merch_type < 0 and merch_type > 4:
                    print("There is no such filter")
                    sleep(0.5)
                    merch_type = 0
            except Exception:
                print("There is no such filter")
                sleep(0.5)
            else:
                os.system("cls")
                min_price = input("Enter min price or pass this: ")
                max_price = input("Enter max price or pass this: ")
                try:
                    if min_price != "":
                        min_price = int(min_price)
                    else:
                        min_price = 0
                    if max_price != "":
                        max_price = int(max_price)
                    else:
                        max_price = 999999
                except Exception:
                    print("You must write number")
                    sleep(0.5)
                else:
                    os.system("cls")
                    min_rating = input("Enter min rating or pass this: ")
                    try:
                        if min_rating != "":
                            min_rating = float(min_rating)
                        else:
                            min_rating = 0.0
                    except Exception:
                        print("You must write number")
                        sleep(0.5)
                    else:
                        while True:
                            os.system("cls")
                            match merch_sort:
                                case 0:
                                    if merch_type == "0":
                                        pretty_print(list(filter(lambda merch: merch["price"] > min_price and merch["price"] < max_price and merch["rating"] > min_rating, merchandise), key=lambda merch: merch["price"]))
                                    else:
                                        pretty_print(list(filter(lambda merch: merch["type"] == merch_types[merch_type] and merch["price"] > min_price and merch["price"] < max_price and merch["rating"] > min_rating, merchandise), key=lambda merch: merch["price"]))
                                case 1:
                                    pretty_print(list(sorted(filter(lambda merch: merch["type"] == merch_types[merch_type] and merch["price"] > min_price and merch["price"] < max_price and merch["rating"] > min_rating, merchandise), key=lambda merch: merch["price"])))
                                case 2:
                                    pretty_print(list(sorted(filter(lambda merch: merch["type"] == merch_types[merch_type] and merch["price"] > min_price and merch["price"] < max_price and merch["rating"] > min_rating, merchandise), key=lambda merch: merch["price"], reverse=True)))
                                case 3:
                                    pretty_print(list(sorted(filter(lambda merch: merch["type"] == merch_types[merch_type] and merch["price"] > min_price and merch["price"] < max_price and merch["rating"] > min_rating, merchandise), key=lambda merch: merch["rating"])))
                                case 4:
                                    if merch_type == 0:
                                        pretty_print(list(sorted(filter(lambda merch: merch["price"] > min_price and merch["price"] < max_price and merch["rating"] > min_rating, merchandise), key=lambda merch: merch["solled"], reverse=True)))
                                    else:
                                        pretty_print(list(sorted(filter(lambda merch: merch["type"] == merch_types[merch_type] and merch["price"] > min_price and merch["price"] < max_price and merch["rating"] > min_rating, merchandise), key=lambda merch: merch["solled"], reverse=True)))
                        
                            print("_____________________________________")
                            print("1 - buy smth")
                            print("0 - get the Hell out")
                            choice = input("Whatcha want? ")
                            if choice == "1":
                                try:
                                    print("")
                                    merch = int(input("Write the merch ID: "))
                                except Exception:
                                    print("There is no such merch")
                                else:
                                    for i in merchandise:
                                        if i["id"] == merch:
                                            user["cart"].append(i["title"])

                            elif choice == "0":
                                print("Get the Hell out!")
                                sleep(0.5)
                                return user
                            else:
                                print("There is no such choice")
                                sleep(0.5)


def view_history(user):
    os.system("cls")
    merch_id = 0
    for i in user["history"]:
        print(merch_id+1, ": ", i)
        i+=1
    print("")
    print("Whatcha want?")
    print("1 - Rate this")
    print("0 - Quit")
    choice = input()
    print("")

    if choice == "1":
        try:
            merch_id = int(input("Write the merch ID: "))
            rate = float(input("Write the rate from 0.0 to 10.0: "))
        except Exception:
            print("You must write number from 0 to 10")
            sleep(0.5)
        else:
            if rate >= 0 and rate <= 10:
                for i in merchandise:
                    if i["title"] == user["history"][merch_id-1]:
                        i["rating"] = round((i["rating"] * (i["solled"]-1) + rate)/i["solled"], 1)
                print("Ok")
                sleep(0.5)
            else:
                print("You must write number from 0 to 10")
    elif choice == "0":
        print("Get the Hell out!")
        sleep(0.5)
        return user
    else:
        print("There is no such choice")
        sleep(0.5)

    return user


def cart(user):
    while True:
        os.system("cls")
        merch_id = 1
        for i in user["cart"]:
            print(merch_id, ": ", i)
            i+= 1
        print("1 - pay for the merchandise")
        print("2 - delete the merchandise")
        print("0 - get the Hell out")
        choice = input("Whatcha want? ")
        print("")

        match choice:
            case "1":
                j = 0
                for i in user["cart"]:
                    j+=1
                    print(f"{j}: {i}")
                try:
                    print("")
                    choice = int(input("Write the merch ID or write 0 to pay for them all: "))
                except Exception:
                    print("There is no such merch")
                    sleep(0.5)
                
                if choice == 0:
                    for i in merchandise:
                        for j in user['cart']:
                            if i["title"] == j:
                                i['solled'] += 1
                                user["spent"] += i["price"] 
                    for i in range(len(user["cart"])):
                        print(i)
                        user["history"].append(user["cart"][i])
                    user["cart"].clear()
                    sleep(5)
                else:
                    for i in merchandise:
                        if i["title"] == user['cart'][choice-1]:
                            i['solled'] += 1
                            user["spent"] += i["price"] 
                    user["history"].append(user["cart"][choice-1])
                    user["cart"].pop(choice-1)
                    sleep(0.5)
            case "2":
                for i in user["cart"]:
                    for j in range(len(user["cart"])):
                        print(f"{j}: {i}")
                try:
                    choice = int(input("Write the merch ID or write 0 to delete them all: "))
                except Exception:
                    print("There is no such merch")
                    sleep(0.5)
                
                if choice == 0:
                    for i in range(len(user["cart"])):
                        user["cart"].pop(i)
                else:
                    user["cart"].pop(choice-1)
            case "0":
                print("byeeeee")
                sleep(0.5)
                break
    return user


def change(user, changed):
    if changed:
        old_pw = input("Enter your current password: ")
        new_pw = input("Enter your new password: ")
        new2_pw = input("Enter your new password again: ")
        if old_pw != user["password"]:
            print("This's not your password!")
            sleep(0.5)
        else:
            if new2_pw != new_pw:
                print("New passwords ain's same")
            else:
                print("Your password's changed")
                sleep(0.5)
                user["password"] = new_pw
                logins[user["id"]]["password"] = new2_pw
    else:
        old_pn = input("Enter your current phone number: ")
        new_pn = input("Enter your new phone number: ")
        if old_pn != user["phone_number"]:
            print("This's not your phone number!")
            sleep(0.5)
        else:
            print("Your phone number's changed")
            sleep(0.5)
            user["phone_number"] = new_pn
            logins[user["id"]]["phone_number"] = new_pn
        pass

    return user


def view_profile(user):
    os.system("cls")
    print(f"Hey, {user["name"]}.")
    print(f"Your role is {user["role"]}")
    print(f"You spent here {user["spent"]}")
    print(f"Here since {user["creations_date"]}")
    print("Whatcha want?")
    print("1 - View your history")
    print("2 - View your cart")
    print("3 - Change your phone number")
    print("4 - Change your password")
    print("0 - Get the Hell out")
    choice = input()
    print("")

    match choice:
        case "1":
            user = view_history(user)
        case "2":
            user = cart(user)
        case "3":
            user = change(user, 0)
        case "4":
            user = change(user, 1)
        case "0":
            print("byeeeee")
            sleep(0.5)

    return user


def update_data(user, data):
    match data:
        case 1:
            while(True):
                os.system("cls")
                print("Whatcha want?")
                print("1 - Add user")
                print("2 - Add merch")
                print("0 - Quit")
                choice = input("")

                match choice:
                    case "1":
                        os.system("cls")
                        new_role = input("Enter the new user role (user or admin): ").lower()
                        new_name = input("Enter the new user login: ")
                        new_phone = input("Enter the new user phone number: ")
                        new_password = input("Enter the new user password: ")
                        creations_date = datetime.datetime.now().strftime('%Y-%m-%d')
                        names = list()
                        phones = list()
                        for i in logins:
                            names.append(i["name"])
                            phones.append(i["phone_number"])
                        if new_name not in names:
                            if new_phone not in phones:
                                if new_role == "user":
                                    logins.append({ 
                                        "role": new_role, 
                                        "name": new_name, 
                                        "phone number": new_phone,
                                        "password": new_password, 
                                        "history": [],
                                        "cart": [],
                                        "creations_date": creations_date,
                                        "spent": 0
                                    })
                                elif new_role == "admin":
                                    logins.append({ 
                                        "role": new_role, 
                                        "name": new_name, 
                                        "phone number": new_phone,
                                        "password": new_password, 
                                        "creations_date": creations_date,
                                    })
                                else:
                                    print("There is only two roles")
                                logins_name[str(len(logins_name))] = new_name
                                logins_phone[str(len(logins_phone))] = new_phone
                                print("")
                                print(f"User {new_name} added")
                                sleep(0.5)

                                print("_____________________________________")
                                print("What do you want?")
                                print("1 - Add one more user")
                                print("0 - Quit")
                                choice = input()

                                if choice == "1":
                                    pass
                                elif choice == "0":
                                    return user
                                else:
                                    print("There is no such choice")
                            else:
                                print("This phone number is already taken")
                        else:
                            print("This login is already taken")
                    case "2":
                        os.system("cls")
                        type = input("Enter the new merch type: ").capitalize().strip()
                        title = input("Enter the new merch title: ").capitalize().strip()
                        price = input("Enter the new merch price: ").strip()
                        date = datetime.datetime.now().strftime('%Y-%m-%d')
                        try:
                            price = int(price)
                        except Exception:
                            print("Price must be number")
                        else:
                            merch_id = []
                            titles = []
                            for i in merchandise:
                                merch_id.append(i["id"])
                                titles.append(i["title"])
                            merch_id = max(merch_id)+1
                            if title not in titles:
                                merchandise.append({
                                    "id": merch_id, 
                                    "type": type, 
                                    "title": title, 
                                    "price": price, 
                                    "rating": 0, 
                                    "date": date, 
                                    "solled" : 0
                                })
                                print("")
                                print(f"Merch {title} added")
                                sleep(0.5)

                                print("_____________________________________")
                                print("What do you want?")
                                print("1 - Add one more merch")
                                print("0 - Quit")
                                choice = input()
                                if choice == "1":
                                    pass
                                elif choice == "0":
                                    return user
                                else:
                                    print("There is no such choice")
                            else:
                                print("Merch with this title already exist")
                                sleep(0.5)
                    case "0":
                        print("Goodbye")
                        sleep(0.5)
                        return user
        case 2:
            while True:
                os.system("cls")
                print("Whatcha want?")
                print("1 - Update user")
                print("2 - Update merch")
                print("0 - Quit")
                choice = input("")

                match choice:
                    case "1":
                        upd_user = input("Enter the login of the user you will be updating: ")
                        upd_id = 0
                        for i in logins:
                            if i["name"] == upd_user:
                                break
                            upd_id += 1 
                        print(f"You choosed {logins[upd_id]["name"]}")
                        print("")
                        print("What are you want to change?")
                        print("1 - Login")
                        print("2 - Phone number")
                        print("3 - Password")
                        print("0 - Quit")
                        choice = input()

                        match choice:
                            case "1":
                                logins[upd_id]["name"] = input("Enter new name: ")
                            case "2":
                                logins[upd_id]["phone_number"] = input("Enter new phone number: ")
                            case "3":
                                logins[upd_id]["password"] = input("Enter new password: ")
                            case "0":
                                break
                        print("")
                        print(f"User updated")
                        sleep(0.5)

                        print("_____________________________________")
                        print("What do you want?")
                        print("1 - Update one more user")
                        print("0 - Quit")
                        choice = input()

                        if choice == "1":
                            pass
                        elif choice == "0":
                            return user
                        else:
                            print("There is no such choice")
                    case "2":
                        print(*list(map(lambda merch: f"\n{merch["id"]}: {merch["title"]} ({merch["type"]}) - price: {merch["price"]}, rating: {merch["rating"]}, date added: {merch["date"]}. Solled: {merch["solled"]}", merchandise)))
                        print("_____________________________________")
                        upd_merch = input("Enter the ID of the merch you will be updating: ")
                        merch_id = ""
                        for i in merchandise:
                            if str(i["id"]) == upd_merch:
                                merch_id = merchandise.index(i)
                        if merch_id != "":
                            print(f"You choosed {merchandise[merch_id]["title"]}")
                            print("")
                            print("What are you want to change?")
                            print("1 - Title")
                            print("2 - Price") 
                            print("0 - Quit")
                            choice = input()

                            match choice:
                                case "1":
                                    merchandise[merch_id]["title"] = input("Enter new title: ")
                                case "2":
                                    merchandise[merch_id]["price"] = input("Enter new price: ")
                                case "0":
                                    break
                            print("")
                            print(f"Merch updated")
                            sleep(0.5)

                            print("_____________________________________")
                            print("What do you want?")
                            print("1 - Update one more merch")
                            print("0 - Quit")
                            choice = input()

                            if choice == "1":
                                pass
                            elif choice == "0":
                                return user
                            else:
                                print("There is no such choice")
                        else:
                            print("There is not such merch")
                            sleep(0.5)
                    case "0":
                        print("Goodbye")
                        sleep(0.5)
                        return user
        case 3:
            while True:
                os.system("cls")
                print("Whatcha want?")
                print("1 - Delete user")
                print("2 - Delete merch")
                print("0 - Quit")
                choice = input("")

                match choice:
                    case "1":
                        os.system("cls")
                        del_user = input("Enter the login of the user you will be deleting: ")
                        del_id = 0
                        for i in logins:
                            if i["name"] == del_user:
                                break
                            del_id += 1 
                        print(f"You choosed {logins[del_id]["name"]}")
                        print("")
                        print("What are you want?")
                        print("1 - Delete")
                        print("0 - Quit")
                        choice = input()
                        print("")

                        if choice == "1":
                            logins.pop(del_id)
                            logins_name.pop(str(del_id))
                            logins_phone.pop(str(del_id))
                            for i in logins_name:
                                i = int(i)
                                print(logins_name)
                                if i > del_id:
                                    logins_name[str(i - 1)] = logins_name[str(i)]
                                    logins_name.pop(str(i))
                            for i in logins_phone:
                                i = int(i)
                                if i > del_id:
                                    logins_phone[str(i - 1)] = logins_phone[str(i)]
                                    logins_phone.pop(str(i))
                            print(f"{logins[del_id]["name"]} been deleted")
                            sleep(0.5)
                            print("_____________________________________")
                            print("What do you want?")
                            print("1 - Delete one more user")
                            print("0 - Quit")
                            choice = input()

                            if choice == "1":
                                pass
                            elif choice == "0":
                                return user
                            else:
                                print("There is no such choice")
                        elif choice == "0":
                            print("Goodbye")
                            sleep(0.5)
                            return user
                        else:
                            print("There is no such choice")
                            sleep(0.5)
                    case "2":
                        print(*list(map(lambda merch: f"\n{merch["id"]}: {merch["title"]} ({merch["type"]}) - price: {merch["price"]}, rating: {merch["rating"]}, date added: {merch["date"]}. Solled: {merch["solled"]}", merchandise)))
                        print("_____________________________________")
                        del_merch = input("Enter the ID of the merch you will be deleting: ")
                        merch_id = ""
                        for i in merchandise:
                            if str(i["id"]) == del_merch:
                                merch_id = merchandise.index(i)
                        if merch_id != "":
                            print(f"You choosed {merchandise[merch_id]["title"]}")
                            print("")
                            print("What are you want?")
                            print("1 - Delete")
                            print("0 - Quit")
                            choice = input()
                            print("")

                            if choice == "1":
                                merchandise.pop(merch_id)
                                for i in logins:
                                    if i["role"] == "user":
                                        if merchandise[merch_id]["title"] in i["cart"]:
                                            i['cart'].pop(i['cart'].index(merchandise[merch_id]['title']))
                                print(f"{merchandise[merch_id]['title']} been deleted")
                                sleep(0.5)
                                print("_____________________________________")
                                print("What do you want?")
                                print("1 - Delete one more merch")
                                print("0 - Quit")
                                choice = input()

                                if choice == "1":
                                    pass
                                elif choice == "0":
                                    return user
                                else:
                                    print("There is no such choice")
                            elif choice == "0":
                                print("Goodbye")
                                sleep(0.5)
                                return user
                            else:
                                print("There is no such choice")
                        else:
                            print("There is not such merch")
                    case "0":
                        print("Goodbye")
                        sleep(0.5)
                        return user


    return user


def view_statistic(user):
    os.system("cls")
    solled = {}
    rated = {}
    spent = {}
    total_spent = []
    for i in merchandise:
        solled[i['solled']] = f"{i["title"]} - {i["solled"]}"
        rated[i["rating"]] = f"{i["title"]} - {i["rating"]}"
        total_spent.append(i["price"]*i["solled"])
    for i in logins:
        if i["role"] == "user":
            spent[i["spent"]] = f"{i["name"]} - {i["spent"]}"

    print(f"Best selling merch: {solled[max(solled)]}")
    print(f"Worst selling merch: {solled[min(solled)]}")
    print("")
    print(f"Best rated merch: {rated[max(rated)]}")
    print(f"Worst rated merch: {rated[min(rated)]}")
    print("")
    print(f"Best customer: {spent[max(spent)]}")
    print(f"Worst customer: {spent[min(spent)]}")
    print("")
    print(f"Total spent: {reduce(lambda x, y: x+y, total_spent)}")
    input(("Press Enter to continue "))

    return user


def view_users(user):
    os.system("cls")
    print(*list(map(lambda login: f"\n{login['name']} - {login["role"]}. Phone number - {login['phone_number']}. Here since {login["creations_date"]}", logins)))
    print("")
    input("Press Enter to continue ")

    return user


logins_name = {
    "0": "ArtisanOfArms",
    "1": "deadweight1988",
    "2": "pizzaman1972",
    "3": "usertest",
    "4": "admintest"
}

logins_phone = {
    "0": "76454234536",
    "1": "73522154252",
    "2": "75238539624",
    "3": "77777777777",
    "4": "78888888888"
}

logins = [
{ 
    "role": "admin", 
    "name": "ArtisanOfArms", 
    "phone_number": "76454234536",
    "password": "Nell45Calliber", 
    "creations_date": "01.02.2005"
},
{ 
    "role": "user", 
    "name": "deadweight1988", 
    "phone_number": "73522154252",
    "password": "Kyrie2005", 
    "history": ["Overture", "Tomboy", "Monkey Business"],
    "cart": ["Overture"],
    "creations_date": "04.07.2009",
    "spent": 6500
},
{ 
    "role": "user", 
    "name": "pizzaman1972", 
    "phone_number": "75238539624",
    "password": "strawberrY666", 
    "history": ["Gold Orb", "Kalina Ann II"],
    "cart": ["pizza"],
    "creations_date": "27.09.2010",
    "spent": 20000
},
{ 
    "role": "user", 
    "name": "usertest", 
    "phone_number": "77777777777",
    "password": "password123", 
    "history": ["Gold Orb"],
    "cart": [],
    "creations_date": "01.02.2015",
    "spent": 5000
},
{ 
    "role": "admin", 
    "name": "admintest", 
    "phone_number": "78888888888",
    "password": "password123", 
    "creations_date": "01.02.2015"
},
]

merchandise = [
    {"id": 40, "type": "Devil Breaker", "title": "Overture", "price": 500, "rating": 8.5, "date": "04.05.2010", "solled" : 27},
    {"id": 65, "type": "Orb", "title": "Blue Orb", "price": 500, "rating": 8.8, "date": "16.05.2005", "solled" : 5},
    {"id": 12, "type": "Devil Breaker", "title": "Gerbera", "price": 500, "rating": 7.0, "date": "19.05.2010", "solled" : 16},
    {"id": 41, "type": "Service", "title": "Transportation", "price": 15000, "rating": 0.6, "date": "01.04.2010", "solled" : 6},
    {"id": 20, "type": "Devil Breaker", "title": "Punch Line", "price": 1000, "rating": 4.3, "date": "10.05.2010", "solled" : 4},
    {"id": 24, "type": "Orb", "title": "Gold Orb", "price": 5000, "rating": 9.6, "date": "24.06.2005", "solled" : 3},
    {"id": 14, "type": "Weapon", "title": "Kalina Ann", "price": 10000, "rating": 9.9, "date": "14.08.2005", "solled" : 1},
    {"id": 46, "type": "Devil Breaker", "title": "Buster arm", "price": 3500, "rating": 9.1, "date": "14.06.2010", "solled" : 8},
    {"id": 35, "type": "Weapon", "title": "Kalina Ann II", "price": 15000, "rating": 9.4, "date": "15.06.2010", "solled" : 2},
    {"id": 6, "type": "Service", "title": "Equipment repair", "price": 10000, "rating": 8.7, "date": "2.09.2005", "solled" : 34},
    {"id": 61, "type": "Devil Breaker", "title": "Tomboy", "price": 1000, "rating": 6.9, "date": "06.06.2010", "solled" : 11},
    {"id": 44, "type": "Service", "title": "Equipment upgrade", "price": 20000, "rating": 8.0, "date": "04.04.2006", "solled" : 5},
    {"id": 78, "type": "Weapon", "title": "Red Queen II", "price": 50000, "rating": 7.9, "date": "07.08.2010", "solled" : 0},
    {"id": 27, "type": "Devil Breaker", "title": "Ragtime", "price": 3500, "rating": 8.7, "date": "27.06.2010", "solled" : 4},
    {"id": 30, "type": "Devil Breaker", "title": "Monkey Buisness", "price": 5000, "rating": 10.0, "date": "30.06.2010", "solled" : 99},
    {"id": 25, "type": "Orb", "title": "Purple Orb", "price": 1000, "rating": 7.4, "date": "16.05.2005", "solled" : 9},
]


shop = True
while shop:
    os.system("cls")
    print("Welcome to Nico's shop!")

    shopping = True

    login = input("Enter login or phone number: ")
    password = input("Enter password: ")
    error = 2
    try:
        user = logins[int("".join(list(filter(lambda key: logins_name[key] == login, logins_name))))]
        user["id"] = int("".join(list(filter(lambda key: logins_name[key] == login, logins_name))))
    except Exception:
        pass
    else:
        error -= 1

    try:
        user = logins[int("".join(list(filter(lambda key: logins_phone[key] == login, logins_phone))))]
        user["id"] = int("".join(list(filter(lambda key: logins_phone[key] == login, logins_phone))))
    except Exception:
        pass
    else:
        error -= 1
    
    if error == 1:
        if user["password"] == password:
            error -= 1

    if error != 0:
        print("Login, number or password entered incorrectly!")
        sleep(0.5)
    else:
        while shopping:
            os.system("cls")
            if user["role"] == "user":
                sleep(0.5)
                print(f"Heya {user["name"]}")
                print("Whatcha want?")
                print("1 - View merchandise")
                print("2 - Search")
                print("3 - Sort and filters")
                print("4 - View your profile")
                print("5 - Logout")
                print("0 - Get the Hell out")
                choice = input()

                match choice:
                    case "1":
                        user = buy(user)
                    case "2":
                        user = search(user)
                    case "3":
                        user = sortnfilter(user)
                    case "4":
                        user = view_profile(user)
                    case "5":
                        print("Flock off")
                        sleep(0.5)
                        shopping = False
                    case "0":
                        print("Flock off")
                        sleep(0.5)
                        shop = False
                        shopping = False
                    case _:
                        print("There is no such choice")
                        sleep(0.5)
            else:
                print(f"Greetings {user["name"]} ({user["role"]})")
                print("What do you want?")
                print("1 - Adding data")
                print("2 - Updating data")
                print("3 - Deleting data")
                print("4 - View statistic")
                print("5 - View users")
                print("6 - Logout")
                print("0 - Quit")
                choice = input()

                match choice:
                    case "1":
                        user = update_data(user, 1)
                    case "2":
                        user = update_data(user, 2)
                    case "3":
                        user = update_data(user, 3)
                    case "4":
                        user = view_statistic(user)
                    case "5":
                        user = view_users(user)
                    case "6":
                        print("Goodbye")
                        sleep(0.5)
                        shopping = False
                    case "0":
                        print("Goodbye")
                        sleep(0.5)
                        shop = False
                        shopping = False
                    case _:
                        print("There is no such choice")
                        sleep(0.5)
