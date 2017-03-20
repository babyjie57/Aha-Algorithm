#-*- coding:utf8 -*-

def bucketsort(arr):
    result = []
    for i in range(len(arr)):
        result.append(0)
    for num in arr:
        result[num] += 1
    return result

if __name__ == "__main__":
    n = raw_input("please input a num: ")
    arr = []
    for i in range(int(n)):
        arr.append(int(raw_input("please input n numbers:  ")))
    arr = bucketsort(arr)
    for i in range(len(arr)):
        if arr[i] != 0:
            step = arr[i]
            while step > 0:
                print i,
                step -= 1



