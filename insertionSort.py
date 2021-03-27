def insertSort(lst):
    for i in range(len(lst)):
        if i == 0:
            continue
        for j in range(i,0,-1):
            if lst[j]<lst[j-1]:
                lst[j],lst[j-1] = lst[j-1],lst[j]
            else:
                break

lst = [3, 3, 4, 6, 5, 7, 9, 11, 3, 32, 13, 8]
insertSort(lst)
print(lst)