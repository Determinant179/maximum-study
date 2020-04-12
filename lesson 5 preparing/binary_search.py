lists = [1, 3, 5, 7, 9, 11, 13, 15] 

def binary_search (list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        guess = int((low + high + 1) / 2)
        print("From ", low, " to ", high, ", now is ", guess)
        if item == list[guess]:
            return guess
        elif item < list[guess]:
            high = guess
        else:
            low = guess
        print("From ", low, " to ", high, ", now is ", guess)
    return 0
            

print(binary_search(lists, 11))
