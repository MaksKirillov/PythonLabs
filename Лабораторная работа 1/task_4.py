users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

visits_dict = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

unique_users = set(users)
visits_dict["Общее количество"] = len(users)
visits_dict["Уникальные посещения"] = len(unique_users)
print(visits_dict)
