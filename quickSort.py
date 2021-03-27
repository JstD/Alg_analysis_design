def quickSort(left,right,lst):
    if left >= right or left<0:
        return
    else:
        pivot = left
        # partition
        j = left
        k = right
        while True:
            for x in range(j+1,right+1):
                if lst[pivot] <= lst[x]:
                    j = x
                    break
            else:
                j = right

            for x in range(k,left,-1):
                if lst[pivot] >= lst[x]:
                    k = x
                    break
                else:
                    k = left
                    
            if j<k:
                lst[j],lst[k] = lst[k],lst[j]
            else:
                break
        lst[k],lst[pivot] = lst[pivot],lst[k]
        # print(lst,k)
        quickSort(left,k-1,lst)
        quickSort(k+1,right,lst)

lst = [3, 3, 4, 6, 5, 7, 9, 11, 3, 32, 13, 8]
quickSort(0,len(lst)-1,lst)
print(lst)