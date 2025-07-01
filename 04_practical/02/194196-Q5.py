numbers = [15, 30, 85, 65, 99]

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

print(linear_search(numbers, 85))
print(linear_search(numbers, 0))