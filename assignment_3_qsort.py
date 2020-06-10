def swap(arr, i, j):
    if len(arr) < 2:
        return

    if i < 0 or i >= len(arr) or j < 0 or j >= len(arr):
        return

    if i == j:
        return

    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

    return


def partition(arr, low, high):
    if low >= high:
        return -1

    pi = low
    li = low + 1
    ri = high

    while ri >= li:

        if arr[li] > arr[pi]:
            swap(arr, ri, li)

            ri -= 1
        else:
            li += 1

    pi = li - 1
    swap(arr, low, pi)

    return pi


def q_sort_iteration(arr, low, high):
    if low >= high:
        return
    regions = [[low, high]]
    i = 0
    while i < len(regions):
        low = regions[i][0]
        high = regions[i][1]
        p = partition(arr, low, high)
        if p != -1:
            regions.append([low, p - 1])
            regions.append([p + 1, high])
        i += 1
    return


def qsort_recursion(arr, low, high):
    if low >= high:
        return
    p = partition(arr, low, high)
    qsort_recursion(arr, low, p - 1)
    qsort_recursion(arr, p + 1, high)
    return


arr = [9, 5, 3, 1, 7, 8, 2, 6, 12, 4]
q_sort_iteration(arr, 0, len(arr) - 1)
print(arr)

arr = [13, 21, 56, 2, 0, 7, 1, 8, 4, 3]
qsort_recursion(arr, 0, len(arr) - 1)
print(arr)
