import json

with open('dump.json', 'r', encoding='utf-8') as file:
    data = json.load(file)#чтение данных из файла в формате JSON и преобразование их в объекты Python

#запрос номера квалификации у пользователя
numb = input("Введите номер квалификации: ")

print("\n=============== Результат поиска ===============")
for item in data:
    if item['model'] == 'data.skill' and item['fields']['code'].startswith(numb):#startswith проверяет, начинается ли строка на указанную подстроку
        print(f"{item['fields']['code']} >> Квалификация {item['fields']['title']}")
        found = True
    elif item['model'] == 'data.specialty' and item['fields']['code'].startswith(numb):
        print(f"{item['fields']['code']} >> Специальность {item['fields']['title']}")

if not found:
    print("============== Не найдено ===============")