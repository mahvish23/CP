""" ower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
1) Only one disk can be moved at a time.
2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
3) No disk may be placed on top of a smaller disk.
"""
def toh(n,source,aux,dest):
    if n==1:
        print(f"move {n} disk from {source} to {dest}")
        return
    toh(n-1,source,dest,aux)
    print(f"move {n} disk from {source} to {dest}")
    toh(n-1,aux,source,dest)
toh(3,"A","B","C")