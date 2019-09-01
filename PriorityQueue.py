# Python Implementation for Priority Queue -


def getlargest(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i].f_value < arr[l].f_value:
        largest = l

    if r < n and arr[largest].f_value < arr[r].f_value:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        getlargest(arr, n, largest)


def queue(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        getlargest(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        getlargest(arr, i, 0)
    return arr
