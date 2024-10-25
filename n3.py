# Задаем список игроков
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Определяем общее количество игроков
total_players = len(list_players)

# Вычисляем индекс середины
middle_index = total_players // 2

# Используем слайсирование для разделения на две команды
first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

# Выводим команды
print("Первая команда:", first_team)
print("Вторая команда:", second_team)