print("Введите координаты клеток:")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
    
print((x1+3==x2 and y1+1==y2) or (x1+3==x2 and y1-1==y2) or (x1-3==x2 and y1+1==y2) or (x1-3==x2 and y1-1==y2) or (x1+1==x2 and y1+3==y2) or (x1+1==x2 and y1-3==y2) or (x1-1==x2 and y1+3==y2) or (x1-1==x2 and y1-3==y2))