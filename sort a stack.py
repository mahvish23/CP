"""" SORT A STACK """
def insertstack(arr,ele):
    if len(arr)==0 or arr[-1]<=ele:
        arr.append(ele)
        return
        val=arr.pop()
        insertstack(arr,ele)
        arrr.append(val)
def sortstack(arr):
    if len(arr)==1:
        return
    ele=arr.pop()
    sortstack(arr)
    insertstack(arr,ele)
a=list(map(int,input().split()))
sortstack(a)
a.reverse()
print(a)
