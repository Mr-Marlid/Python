def oborot(x):
    y = int(input())
    if y != 0:
        oborot(y)
    print(y)



oborot(0)
