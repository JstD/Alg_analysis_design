def hanoi(n,beg,aux,end):
    if n ==1:
        print(beg,'to',end)
    else:
        hanoi(n-1,beg,end,aux)
        print(beg,'to',end)
        hanoi(n-1,aux,beg,end)

hanoi(8,'A','B','C')