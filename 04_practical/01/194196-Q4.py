def sum_up_to(n, acc=0):
    if n == 0:
        return acc
    return sum_up_to(n - 1, acc + n)

print(sum_up_to(3))