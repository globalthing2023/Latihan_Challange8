for i in range(1, 20, 2):
    x =  "+"*i
    print(f"{x:^34}")

for i in range(17, 0,-2):
    x =  "+"*i
    print(f"{x:^34}")

for i in range(10):
    x = "+" * i
    y = "+" * i
    print(f"{x:<10}",f"{y:>10}")

for i in range(10, 1, -1):
    x = "+" * i
    y = "+" * i
    print(f"{x:<10}",f"{y:>10}")
