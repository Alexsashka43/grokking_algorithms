def quicksort(list_num):
    if len(list_num) < 2:
        return list_num
    else:
        num = list_num[0]
        less = [i for i in list_num[1:] if i <= num]
        greater = [i for i in list_num[1:] if i > num]
        return quicksort(less) + [num] + quicksort(greater)


if __name__ == '__main__':
    print(quicksort([10, 3, 5, 2, 7, 8]))
