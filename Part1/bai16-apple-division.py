# There are n apples with known weights. Your task is to divide the apples into two groups so that the difference between the weights of the groups is minimal.
# Input
# The first input line has an integer n: the number of apples.
# The next line has n integers p_1,p_2,\dots,p_n: the weight of each apple.
# Output
# Print one integer: the minimum difference between the weights of the groups.
# Constraints

# 1 \le n \le 20
# 1 \le p_i \le 10^9

# Example
# Input:
# 5
# 3 2 7 4 1

# Output:
# 1

# Explanation: Group 1 has weights 2, 3 and 4 (total weight 9), and group 2 has weights 1 and 7 (total weight 8).




def calculate(array):
    total_Sum=sum(array)
    dp=[False]*(total_Sum//2+1)
    dp[0]=True
    for weight  in array:
        for j in range(total_Sum//2,weight  - 1,-1):
            if (dp[j-weight ]):
                dp[j]=True
    for j in range(total_Sum//2,-1,-1):
        if dp[j]:
            best_sum  =j
            break
    count = total_Sum - 2 * best_sum
    print(count)

# Example usage
n=int(input().strip())
weights = list(map(int, input().strip().split()))
result = calculate(weights)
