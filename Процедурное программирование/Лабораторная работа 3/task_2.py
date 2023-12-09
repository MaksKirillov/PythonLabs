def find_common_participants(string_first_group, string_second_group, divider=","):
    set_first_group = set(string_first_group.split(divider))
    set_second_group = set(string_second_group.split(divider))
    list_common_participants = list(set_first_group.intersection(set_second_group))
    list_common_participants.sort()
    return list_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
