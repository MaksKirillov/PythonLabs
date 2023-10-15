list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

number_of_all_players = len(list_players)
number_of_players_in_team = number_of_all_players // 2
list_1_team = list_players[:number_of_players_in_team:]
list_2_team = list_players[number_of_players_in_team::]
print(list_1_team)
print(list_2_team)
