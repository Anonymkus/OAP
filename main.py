import asyncio
import aiohttp
import os
from time import sleep

API_URL = "https://api.api-ninjas.com/v1/incometax"
API_KEY = "miRCooTcKsyj8otl2/+I4g==x2iaEEyenc05jaKh"

print("Вывод информации о налогах в США")

while True:
    year = input("Введите год: ")
    if year.isdigit():
        if int(year) >= 1900:
            break
        else:
            print("Год должен быть от 1900")
    else:
        print("Введите число")
    sleep(0.5)
    os.system("cls")

params = {
    "country": "US",
    "year": int(year),
}

headers = {
    "X-Api-Key": API_KEY
}

async def get_tax(session):
    try:
        async with session.get(API_URL, params=params, headers=headers) as response:
            response.raise_for_status()
            data = await response.json()
            display_tax(data)
    except aiohttp.ClientError as e:
        print(f"Ошибка запроса: {e}")

def display_tax(data):
    print(f"=== Налоговая информация cтраны США за {data['year']} ===")

    federals = data["federal"]
    if federals:
        print("Налоговые диапазоны:")
        for federal, details in federals.items():
            print(f"Federal: {federal}")
            for i in details["brackets"]:
                rate = i['rate']
                min_tax = f"{i['min']}$"
                max_tax = f"{i['max']}$"

                print(f" - От {min_tax} до {max_tax}: ставка {round(float(rate)*100, 2)}%")
                
    else:
        print("Нет данных о налоговых диапазонах.")

async def main():
    async with aiohttp.ClientSession() as session:
        await get_tax(session)

if __name__ == "__main__":
    asyncio.run(main())
