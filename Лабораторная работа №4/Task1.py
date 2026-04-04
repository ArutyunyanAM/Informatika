import json # Импорт модуля json

def task() -> float:
    filename = 'input.json'

    # Чтение данных из файла в формате JSON
    with open(filename) as file:
        data = json.load(file)

    proizvedenie = 0 # Переменная для расчета произведения

    # Цикл расчета произведения
    for i in data:
       proizvedenie += i['score'] * i['weight']

    return round(proizvedenie, 3)

# Вывод ответа
print(task())
