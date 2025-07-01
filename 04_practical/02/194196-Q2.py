def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val


print(find_max([3, 5, 1, 9, 2]))
print(find_max([]))