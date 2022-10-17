employee_list = 'Иван', 'Мария', 'Петр', 'Илья', 'Марина', 'Петр', 'Алина', 'Бибочка', 'Алевтина', 'Борис', 'Павел'

def split_to_dict_by_1st_letter(name_list: list):
    res = {}
    for i in name_list:
        if i[0] not in res:
            res[i[0]] = []
        res[i[0]].append(i)
    return res


print(employee_list)
out_dict = split_to_dict_by_1st_letter(list(employee_list)) if not isinstance(employee_list, str)\
      else split_to_dict_by_1st_letter(employee_list.replace(',', '').split())
print()
print(out_dict)