"""SORT AN ARRAY USING RECURSION 
input: a=[1,2,3]
s=[3,2,1]
output:
s=[3,2,1]
"""


def insertarr(arr, ele):
    if len(arr) == 0 or ele >= arr[-1] :
        arr.append(ele)
        return
    val = arr[-1]
    arr.pop()
    insertarr(arr, ele)
    arr.append(ele)


def sortarr(arr):
    if len(a) == 0:
        return
    ele = a.pop()
    sortarr(arr)

    insertarr(arr, ele)


a = list(map(int, input().split()))

sortarr(a)
print(a)
