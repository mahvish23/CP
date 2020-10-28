"""" Reverse an array or a stack """
def reversearr(arr):
    if len(arr)==1:
        return
    ele=arr.pop(0)
    reversearr(arr)
    arr.append(ele)
a=list(map(int,input().split()))
reversearr(a)
print(a)