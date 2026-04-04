# Импорт модуля json и csv
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

# Конвертер из csv в json формат
def task(delimiter=',', line_terminator='\n') -> None:
    # delimiter: разделитель между значениями, по умолчанию ","
    # line_terminator: разделитель строк, по умолчанию "\n"

    # Открываем входной csv файл
    with open(INPUT_FILENAME) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter, lineterminator=line_terminator)
        # Преобразуем объект reader в список словарей
        data = [row for row in reader]

    # Открываем выходной json файл в режиме записи
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    # Открываем созданный json файл
    with open(OUTPUT_FILENAME) as output_f:
        # Вывод содержимого на экран
        for line in output_f:
            print(line, end="")