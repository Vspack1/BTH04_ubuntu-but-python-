"""
Viết chương trình in các số chẵn từ min đến max
"""

min = int(input("Nhap min: "))
max = int(input("Nhap max: "))

#dùng list
arr = list(range(min, max + 1, 2))
print(arr)