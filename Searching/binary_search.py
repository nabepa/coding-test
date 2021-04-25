def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


def bisect_first(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target and (mid == 0 or target > array[mid - 1]):
            return mid
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1

    return None


def bisect_last(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target and (mid == len(array) - 1 or target < array[mid + 1]):
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None
