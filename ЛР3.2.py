def find_common_participants(first_list, second_list, delimiter=","):
    common_people = []
    first_list = first_list.split(delimiter)
    second_list = second_list.split(delimiter)
    for people in first_list:
        if people in second_list:
            common_people.append(people)
    return common_people


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(first_list=participants_first_group,
                               second_list=participants_second_group,
                               delimiter="|"))
