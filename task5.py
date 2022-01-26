import math
x = int(input("Введите число x"))
y = int(input("Введите число y"))
if x>y:
    c = math.sqrt(x*y)
    print(f"Z={c}")
else:
    g = math.log1p(x+y)
    print(f"Z={g}")