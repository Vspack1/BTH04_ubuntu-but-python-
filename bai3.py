"""
Viết chương trình nhập vào một chuỗi, in các từ trong chuỗi trên các dòng, và mỗi
dòng có đánh số thứ tự tăng dần.
"""

arr=[]
s = input("Nhap mot chuoi: ")
arr=s.split()
index=1
for i in arr:
    print(f"{index}:{i}")
    index+=1