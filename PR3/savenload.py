from roles import Guest, Admin
from shop import Merch

def save_data(logins: dict, merchandise: list):
    with open("data.txt", "w", encoding='utf8') as shop_data:
        for i, j in logins.items():
            if j.role == "админ":
                shop_data.write(f"{i}|{j.role}|{j.name}|{j.phone}|{j.password}|{j.creations_date}|" + "\n")
            else:
                if len(j.cart) != 0 and j.cart[0] == "":
                    j.cart.pop(0)
                if len(j.history) != 0 and j.history[0] == "":
                    j.history.pop(0)
                cart = ", ".join(j.cart)
                history = ", ".join(j.history)
                shop_data.write(f"{i}|{j.role}|{j.name}|{j.phone}|{j.password}|{j.creations_date}|{cart}|{history}|{j.spent}|" + "\n")
        for i in merchandise:
            shop_data.write(f"{i.id}|{i.type}|{i.title}|{i.price}|{i.rating}|{i.date}|{i.solled}|" + "\n")


def load_data():
    with open("data.txt", "r", encoding='utf8') as shop_data:
        logins = dict()
        merchandise = list()
        for line in shop_data:
            line = line.split("|")
            if line[1] == "админ" and len(line) == 7:
                logins[line[0]] = Admin(line[1], line[2], line[3], line[4], line[5])
            elif line[1] == "посетитель" and len(line) == 10:
                logins[line[0]] = Guest(line[1], line[2], line[3], line[4], line[5], line[6].split(", "), line[7].split(", "), int(line[8]))
            elif len(line) == 8:
                merchandise.append(Merch(int(line[0]), line[1], line[2], int(line[3]), float(line[4]), line[5], int(line[6])))

    return logins, merchandise

