def linear_search(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return target
        i = i + 1

    return -1


if __name__ == "__main__":
    my_arr = [4, 5, 7, 19, 20, 34, 56, 78, 32, 21, 10, 0]
    target = int(input("Find number: "))

    print(linear_search(my_arr, target))
