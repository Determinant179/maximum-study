
lists = [1, 6, 20, 40, 100, 150, 1000, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1010, 2000, 2456]

def search(list, number):
    i = 0
    while list[i] != number:
        i = i + 1
    return i


def binary_search(list, number):
    low = 0
    high = len(lists) - 1
    i = 0
    while low != high:
        i = i + 1
        guess = int((low + high)/2) + 1
        if list[guess] == number:
            return guess
        elif list[guess] < number:
            low = guess
        else:
            high = guess
        print("low = ", low, "high= ", high, "guess= ", guess)
    print("i = ", i)
    return 0





print(search(lists, 2456))
print(binary_search(lists, 2456))