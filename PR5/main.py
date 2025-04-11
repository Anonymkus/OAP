# C:\Users\soner\Desktop\PRPytnon\PR5\desc.txt

import multiprocessing
import os
import psutil
import time
from threading import Thread

alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
alphabet += alphabet.upper()
max_proc = round(multiprocessing.cpu_count() - (multiprocessing.cpu_count() * (psutil.cpu_percent(interval=1)/100)))
crypted_content = dict()
if os.path.exists("results") == False:
    os.mkdir("results")


def save_result(crypted_content:list):
    with open(f"results/{work_type}crypted_{file_path.split("\\")[-1]}", "w", encoding="utf-8") as file:
        file.write(crypted_content)
    return


def encrypt(content:str, shift:int, id:int, crypted_content):
    res = ""
    for letter in content:
        if letter in alphabet:
            index = alphabet.index(letter)
            index_shifted = (index + shift) % len(alphabet)
            res += alphabet[index_shifted]
        else:
            res += letter
    crypted_content[id] = res


def decrypt(content:str, shift:int, id:int, crypted_content):
    res = ""
    for letter in content:
        if letter in alphabet:
            index = alphabet.index(letter)
            index_shifted = ((index - shift) % len(alphabet) + len(alphabet)) % len(alphabet)
            res += alphabet[index_shifted]
        else:
            res += letter
    crypted_content[id] = res


def crypt(content:str, shift:int, proc_num:int):
    crypted_content = multiprocessing.Manager().dict()
    processes = []
    start = 0
    end = len(content) // proc_num
    for i in range(proc_num):
        if i == proc_num - 1:
            end = len(content)
        if work_type == "en":
            processes.append(multiprocessing.Process(target=encrypt, args=(content[start:end], shift, i, crypted_content)))
        else:
            processes.append(multiprocessing.Process(target=decrypt, args=(content[start:end], shift, i, crypted_content)))
        start = end
        end += len(content) // proc_num
    
    for i in processes:
        i.start()
    for i in processes:
        i.join()

    result = ""
    for i in sorted(crypted_content.items(), key=lambda item: item[0]):
        result += i[1]

    saving_thread = Thread(target=save_result, args=(result,))
    saving_thread.start()
    return
    

def get_content(path:str) -> str:
    with open(path, "r", encoding="utf-8") as content:
        return content.read()


if __name__ == "__main__":
    global file_path, work_type
    while True:
        os.system("cls")
        print("Шифратор Цезаря")
        print("Выберите действие:\n1 - Зашифровать\n2 - Расшифровать\n0 - Выйти")
        choice = input()
        match choice:
            case "0":
                print("Выход...")
                time.sleep(1)
                break
            case "1":
                work_type = "en"
            case "2":
                work_type = "de"
            case _:
                print("Ошибка: выбранного действия нет.")
                time.sleep(0.5)
                continue
        print("Введите путь до файла, которого нужно зашифравать: ")
        file_path = input()
        if os.path.exists(file_path) == False:
            print("Ошибка: файл не найден.")
            time.sleep(1)
            continue
        try:
            print("Введите ключ для шифра: ")
            shift = int(input())
            print("Введите количество процессов для шифрования: ")
            proc_num = int(input(f"от 1 до {max_proc}: "))
            if proc_num > max_proc or proc_num < 1:
                print("Ошибка: Неправильное числов процессов.")
                time.sleep(1)
                continue
        except Exception:
            print("Ошибка: Неправильный тип данных.")
            time.sleep(1)
            continue

        content = get_content(file_path)
        crypt(content, shift, proc_num)
        input(f"Файл сохранен в results/{work_type}crypted_{file_path.split("\\")[-1]}")

