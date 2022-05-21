import time


def linear_search(list, item):
    global t1
    t1 = time.perf_counter()
    for i in range(len(list)):
        if list[i] == item:
            elapsed_time1 = time.perf_counter() - t1
            print("elapsed time for linear search!:", elapsed_time1)
            return i
    return None

""" binary  """
def binary_search(list, item):
    global t2
    t2 = time.perf_counter()
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end)//2
        guess = list[mid]
        if guess == item:
            elapsed_time2 = time.perf_counter() - t2
            print("binary search!:", elapsed_time2)
            return mid
        if guess > item:
            end = mid - 1
        else:
            start = mid + 1
    return None


list = [ 2, 12, 13, 15, 23, 31, 33, 37, 45, 67, 68, 77, 99]

print(linear_search(list, 77))
print(binary_search(list, 77))

