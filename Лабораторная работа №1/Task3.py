list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_index = len(list_players) // 2 # Ищем середину списка

first_team = list_players[:middle_index] # Распределяем первую половину игроков в одну команду
second_team = list_players[middle_index:] # Распределяем вторую половину игроков в одну команду

# Выводим список игроков
print(first_team)
print(second_team)
