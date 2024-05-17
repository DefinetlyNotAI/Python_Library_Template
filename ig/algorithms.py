def total_list(lst):
    return sum(lst)


def max_of_list(lst):
    return max(lst)


def min_of_list(lst):
    return min(lst)


def average_of_list(lst):
    return sum(lst) / len(lst)


def linear_search(lst, target):
    for i, element in enumerate(lst):
        if element == target:
            return i
    return -1


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
