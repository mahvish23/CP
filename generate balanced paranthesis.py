"""
Given an integer N representing the number of pairs of parentheses, the task is to generate all combinations of
well-formed(balanced) parentheses.
Example 1:
Input: N = 3
Output: ((()))
        (()())
        (())()
        ()(())
        ()()()
Example 2:
Input: N = 1
Output: ()
"""


def solve(opb, clb, op, a):
    if opb == clb == 0:
        a.append(op)
        return
    if opb != 0:
        
        op2 = op+"("
        solve(opb - 1, clb, op2 ,a)
    if opb < clb:

        op1 =op+ ")"

        solve(opb, clb - 1, op1, a)


def AllParenthesis(n):
    # code here
    opb = n
    clb = n
    op = ""
    a = []
    solve(opb, clb, op, a)
    return a


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    for i in range(0, t):
        n = int(input())
        result = AllParenthesis(n)
        result.sort()
        for i in range(0, len(result)):
            print(result[i])