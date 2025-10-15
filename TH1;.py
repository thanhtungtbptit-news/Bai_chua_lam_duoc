a=0
while a <= 0:
    a=int(input("Nhập 1 số nguyên dương: "))
total = 0    
for i in range (1,a+1):
    total += i
if total % 2 == 0:
    print("Tổng từ 1 đến ",a,"bằng ",total,"là số chẵn")
else :
    print("Tổng từ 1 đến ",a,"bằng ",total,"là số lẻ")    

