arrEn = ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]
arrVn = ["Tháng 1", "Tháng 2", "Tháng 3", "Tháng 4", "Tháng 5", "Tháng 6",
         "Tháng 7", "Tháng 8", "Tháng 9", "Tháng 10", "Tháng 11", "Tháng 12"]

for i in range(len(arrEn)):
    e = arrEn[i]
    v = arrVn[i]
    print(f"{e:<20} {v:<20}")