def find_common_participants(first_list, second_list, delimiter_=","):
    first_list = set(first_list.split(delimiter_))
    second_list = set(second_list.split(delimiter_))
    common_people = sorted(list(first_list.intersection(second_list)))
    return common_people


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,
                               participants_second_group, "|"))
