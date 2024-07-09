# Your task is to count for k=1,2,\ldots,n the number of ways two knights can be placed on a k \times k chessboard so that they do not attack each other.
# Input
# The only input line contains an integer n.
# Output
# Print n integers: the results.
# Constraints

# 1 \le n \le 10000

# Example
# Input:
# 8

# Output:
# 0
# 6
# 28
# 96
# 252
# 550
# 1056
# 1848


def calculate(n):
    sum_all=n*(n+1)//2

    if sum_all % 2 != 0:
        print("NO")
        return 
    else:
        print("YES")
        target_sum=sum_all//2
        curr_sum=0
        set1 = []
        set2 = []
        for num in range(n,0,-1):
            if(curr_sum+num<=target_sum):
                set1.append(num)
                curr_sum+=num
            else:
                set2.append(num)
        
        # print(len(set1))
        # for result in set1:
        #     print(result)
        # print(len(set2))
        # for result in set2:
        #     print(result)
        print(len(set1))
        print(" ".join(map(str, set1)))
        print(len(set2))
        print(" ".join(map(str, set2)))
n = int(input().strip())
calculate(n)




