import json 

kvalf = input("Введите номер квалификации: ")  
find = False 

with open("dump.json", 'r', encoding = 'utf-8') as file:
    read_file = json.load(file)   
    for skill in read_file: 
        if skill.get("model") == "data.skill":
            if skill["fields"].get("code") == kvalf:  
                skill_code = skill["fields"].get("code") 
                skill_title = skill["fields"].get("title")  
                skill_specialty=skill["fields"].get("specialty")
                find = True

if not find:  
    print(" Не найдено ".center(60, "=")) 
    exit() 

for specialty in read_file:
    if specialty.get("model") == "data.specialty": 
        specialty_code = specialty["fields"].get("code")  
        specialty_pk = specialty.get("pk") 


        if skill_specialty == specialty_pk:
            specialty_title = specialty["fields"].get("title") 
            specialty_educational = specialty["fields"].get("c_type") 
            specialty_c = specialty["fields"].get("code")


else:
    print("\n", " Найдено ".center(80, "="),'\n')
    print(f"{specialty_c} >> Специальность '{specialty_title}', {specialty_educational}") 
    print(f"{kvalf} >> Квалификация '{skill_title}'") 