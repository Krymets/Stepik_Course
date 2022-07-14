a = float(input())
b = float(input())

EMT = a / (b*b)
if 18.4 < EMT < 25.1:
    print("Оптимальная масса")
elif EMT > 25:
    print("Избыточная масса")
else:
    print("Недостаточная масса") #