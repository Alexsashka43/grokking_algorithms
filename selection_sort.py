def find_smallest(arr):
    smallest = arr[0]
    smallest_ind = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_ind = i
    return smallest_ind


def selection_sort_first(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def selection_sort_second(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr


def selection_sort_third(arr):
    for i, e in enumerate(arr):
        mn = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[mn] = arr[mn], e
    return arr


if __name__ == '__main__':
    print(selection_sort_third([5, 3, 6, 2, 10]))
