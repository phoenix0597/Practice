# Задача 2. Игроки
# Есть готовый словарь игроков, у каждого игрока есть имя, команда, в которой он играет,
# а также его текущий статус, в котором указано, отдыхает он, тренируется или путешествует:
#
# players_dict = {
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
#
# Напишите программу, которая выводит на экран следующие данные в разных строках:
# Все члены команды А, которые отдыхают.
# Все члены команды B, которые тренируются.
# Все члены команды C, которые путешествуют.

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

state_list = {
    "Rest": "отдыхают",
    "Training": "тренируются",
    "Travel": "путешествуют"
}

team_order = ["A", "B", "C"]
index = 0
for state in state_list:
    print(f"Все члены команды {team_order[index]}, которые {state_list[state]}: ")
    # for key, player in players_dict.items(): - так тоже можно
    for player in players_dict.values():
        if player['team'] == team_order[index] and player['status'] == state:
            print(player['name'])
    index += 1
