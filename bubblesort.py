#-*- coding:utf8 -*-

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)-i):
            if arr[j-1] > arr[j]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
    return arr



if __name__ == '__main__':
    arr = []
    for i in range(5):
        arr.append(int(raw_input("please input a number: ")))
    print arr
    arr = bubblesort(arr)
    for i in range(len(arr)):
        print arr[i],