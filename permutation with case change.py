"""
Print all permutations of a string keeping the sequence but changing cases.
Examples:
Input : ab
Output : AB Ab ab aB
Input : ABC
Output : abc Abc aBc ABc abC AbC aBC ABC
"""
def solve(s,outp,i):
    if i==len(s):
        print(outp,end=" ")
        return
    solve(s,outp+s[i],i+1)
    solve(s,outp+(s[i].upper()),i+1)

s=input()
s.lower()
outp=""
solve(s,outp,0)