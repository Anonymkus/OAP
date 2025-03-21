def save_data(users: dict, ids: dict):
    with open("data.txt", "w", encoding='utf8') as data:
        for i, j in users.items():
            data.write(f"u/{i}/{j}/" + "\n")
        for i, j in ids.items():
            data.write(f"id/{i}/{j}/" + "\n")


def load_data():
    with open("data.txt", "r", encoding='utf8') as data:
        users = dict()
        ids = dict()
        for line in data:
            line = line.split("/")
            if line[0] == "u":
                users[line[1]] = line[2]
            else:
                ids[line[1]] = int(line[2])
        return users, ids              
        