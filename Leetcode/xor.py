def solve(A, B):
    arr = []
    for a, b in B:
        # Step 1: XOR query intergers together. 
        res = f"{a ^ b:b}"
        # Step 2: Find if string representation of step 1 result is in the string A
        print(A.find(res))
        loc = A.find(res)
        if loc != -1:
            arr.append([loc + 1, loc + len(res)])
        else:
            arr.append([-1, -1])
    return arr

A = "0100"
B = [[5, 7], [5, 5]]
print(solve(A, B))