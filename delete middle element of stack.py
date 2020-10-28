""" Given a stack with PUSH(),POP(),EMPTY() operations, delete the middle of the stack without using any additional data structure.
Middle: ceil(size_of_stack/2.0)


Example 1:

Input:
Stack = {1, 2, 3, 4, 5}
Output:
ModifiedStack = {1, 2, 4, 5}
Explanation:
As the number of elements is 5 ,
hence the middle element will be the 3rd
element which is deleted

Example 2:

Input:
Stack = {1 2 3 4}
Output:
ModifiedStack = {1 3 4}
Explanation:
As the number of elements is 4 ,
hence the middle element will be the 2nd

"""
def deletemidelement(arr,k):
    if k==1:
        a.pop(0)
        return
    ele=arr.pop(0)
    print(ele)
    deletemidelement(arr,k-1)
    arr.insert(0,ele)
a=list(map(int,input().split()))
n=len(a)
k=n//2
deletemidelement(a,k)
print(a)
