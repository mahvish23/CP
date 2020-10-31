def solve(s, inp, i):
    if i == len(s):
        print(f"({inp})",end=" ")
        return
    solve(s, inp+" "+s[i], i + 1)
    solve(s, inp+s[i], i + 1)


s = input()
inp = ""
inp += s[0]
solve(s, inp, 1)