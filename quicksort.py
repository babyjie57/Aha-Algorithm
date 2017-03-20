#-*- coding:utf8 -*-
def quicksort(left, right):

    if left > right:
        return
    temp = a[left]
    i = left
    j = right
    while i != j:
        while a[j] >= temp and i < j:
            j -= 1
        while a[i] <= temp and i < j:
            i += 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[left] = a[i]
    a[i] = temp

    quicksort(left, i-1)
    quicksort(i+1, right)

if __name__ == '__main__':
    # n = raw_input("please input a number: ")
    # for k in range(int(n)):
    #     a.append(int(raw_input("please input n numbers: ")))
    a = [3, 10 , 2 ,2,2,2,2,2,2,4,4,7,8,9,0,0,4 , 6, 2, 8]
    quicksort(0, len(a)-1)
    for i in range(len(a)):
        print a[i],