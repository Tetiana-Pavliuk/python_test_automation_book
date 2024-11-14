def bubble_sorting_asc(list):
    size = len(list)
    temp = 0
    for i in range(size - 1):
        for j in range(size - i - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list


def bubble_sorting_desc(list):
    size = len(list)
    temp = 0
    for i in range(size - 1):
        for j in range(size - i - 1):
            if list[j] < list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list

def bubble_sorting_early_stopping(list):
    n = len(list)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
        if not swapped:
            break
    return list

my_list = [66, 13, 44, 55, 1, 7, 8]
sorted_list_asc = bubble_sorting_asc(my_list.copy())
print("Sorted in ascending order:", sorted_list_asc)

sorted_list_desc = bubble_sorting_desc(my_list.copy())
print("Sorted in descending order:", sorted_list_desc)

sorted_list_early = bubble_sorting_early_stopping(my_list)
print("Sorted with early stopping:", sorted_list_early)
