# A permutation of integers 1,2,\ldots,n is called beautiful if there are no adjacent elements whose difference is 1.
# Given n, construct a beautiful permutation if such a permutation exists.
# Input
# The only input line contains an integer n.
# Output
# Print a beautiful permutation of integers 1,2,\ldots,n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".
# Constraints

# 1 \le n \le 10^6

# Example 1
# Input:
# 5

# Output:
# 4 2 5 3 1
# Example 2
# Input:
# 3

# Output:
# NO SOLUTION

def calculate(n):
    if n==1:
        print(1)
        return
    elif  n>=2 and n<=3:
        print ("NO SOLUTION ")
        return
    even=[]
    odd=[]
    for i in range(2,n+1,2):
        even.append(i)
    for i in range(1,n+1,2):
        odd.append(i)
    permutation=even+odd
    print(" ".join(map(str, permutation)))
n = int(input().strip())
calculate(n)