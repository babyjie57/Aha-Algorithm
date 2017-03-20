#-*- coding:utf8 -*-

def bucketsort(arr):
    result = []
    for i in range(len(arr)):
        result.append(0)
    for num in arr:
        result[num] += 1
    return result

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,8,7,7,7,7,8,9,0,2,1]
    arr = bucketsort(arr)
    for i in range(len(arr)):
        if arr[i] != 0:
            step = arr[i]
            while step > 0:
                print i,
                step -= 1



