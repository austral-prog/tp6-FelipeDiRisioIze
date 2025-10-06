# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    indices_to_remove = [0, 4, 5]
    result = []
    for i in range(len(list_to_remove_elements)):
        if i not in indices_to_remove:
            result.append(list_to_remove_elements[i])
    return result


def add_elements(list_to_add_elements):
    return ['Pink'] + list_to_add_elements + ['Yellow']


def is_empty(list_to_check):
    return len(list_to_check) == 0


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) > 2 and len(list_to_compare2) > 2:
        return list_to_compare1[2] == list_to_compare2[2]
    return False


def list_of_lists(list_of_lists_to_modify):
    result = []

    sublist1 = list_of_lists_to_modify[0][:2]
    result.append(sublist1)

    sublist2 = list_of_lists_to_modify[1][1:4]
    result.append(sublist2)

    sublist3 = list_of_lists_to_modify[2][-2:]
    result.append(sublist3)

    return result

