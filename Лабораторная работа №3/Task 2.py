def find_common_participants(str1,str2,char = ','): # Функция поиска пересечений

    data1 = str1.split(char) # Разделение 1-ой строки на список
    data2 = str2.split(char) # Разделение 2-ой строки на список
    answer = []

    for i in data1:
        if i in data2: # Проверка на наличие слова во 2-ом списке
            answer += [i]
    
    return sorted(answer) # Вывод отсортированного списка


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group, "|"))
