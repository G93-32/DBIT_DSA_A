def find_min(lst):
    if not lst:
        return None
    min_val = lst[0]
    for num in lst[1:]:
        if num < min_val:
            min_val = num
    return min_val


print(find_min([3, 5, 1, 9, 2]))
print(find_min([]))