def linear_search(arr, search):  # for
    for i in range(len(arr)):
        if arr[i] == search:
            return True
    return False


linear_search([3, 110, 8, 13, 2], 5)  # False 返還
linear_search([3, 110, 8, 13, 2], 13)  # True 返還