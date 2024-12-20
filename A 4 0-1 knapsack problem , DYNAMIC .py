def knapSack(W, wt, val, n):
    dp = [0 for i in range(W + 1)]
    
    
    for i in range(1, n + 1):
        
        for w in range(W, 0, -1):
            if wt[i - 1] <= w:
                dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])
    
    return dp[W]


W = []
V = []


num = int(input("Enter the number of weights or values required: \n"))


for i in range(num):
    n = int(input(f"Enter weight {i+1} : "))
    W.append(n)

print("\n")


for i in range(num):
    n = int(input(f"Enter value {i+1} : "))
    V.append(n)

print("\n")


M = int(input("Enter the cost: "))
n = len(V)

print("\n")


print(knapSack(M, W, V, n))
