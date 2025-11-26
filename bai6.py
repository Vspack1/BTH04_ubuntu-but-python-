def min_value(*args):
    min_val = min(args) if args else None
    return min_val

# gọi hàm
min1 = min_value(3, 1, 4, 1, 5, 9)
min2 = min_value(-7, -1, -5, -3)
min3 = min_value(42)
min4 = min_value()

print(min1)
print(min2)
print(min3)
print(min4)