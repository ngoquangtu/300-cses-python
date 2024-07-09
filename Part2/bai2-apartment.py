# There are n applicants and m free apartments. Your task is to distribute the apartments so that as many applicants as possible will get an apartment.
# Each applicant has a desired apartment size, and they will accept any apartment whose size is close enough to the desired size.
# Input
# The first input line has three integers n, m, and k: the number of applicants, the number of apartments, and the maximum allowed difference.
# The next line contains n integers a_1, a_2, \ldots, a_n: the desired apartment size of each applicant. If the desired size of an applicant is x, he or she will accept any apartment whose size is between x-k and x+k.
# The last line contains m integers b_1, b_2, \ldots, b_m: the size of each apartment.
# Output
# Print one integer: the number of applicants who will get an apartment.
# Constraints

# 1 \le n, m \le 2 \cdot 10^5
# 0 \le k \le 10^9
# 1 \le a_i, b_i \le 10^9

# Example
# Input:
# 4 3 5
# 60 45 80 60
# 30 60 75

# 45 60 60 80
# 30 60  75


# Output:
# 2

# def calculate(n,array1,array2):
#     array1.sort()
#     array2.sort()
#     mergeArray=array1+array2
#     count=0
#     right=n
#     left=0

#     while left<right and right < len(mergeArray):
#         if abs(mergeArray[left]-mergeArray[right])<=5:
#             count+=1
#             left+=1
#             right+=1
#         elif mergeArray[left]- mergeArray[right]>5:
#             right+=1
#         elif mergeArray[left]-mergeArray[right] <-5:
#             left+=1
#     print(count)

def calculate(n,m,k,array1,array2):
    left=0
    right=0
    count=0
    array1.sort()
    array2.sort()
    while(left<n and right<m):
        if(array1[left]<array2[right]-k):
            left+=1
        elif(array1[left]>array2[right]+k):
            right+=1
        else:
            left+=1
            right+=1
            count+=1
    print(count)




n, m, k = map(int, input().split())
array2 = list(map(int, input().split()))
array3 = list(map(int, input().split()))
calculate(n,m,k,array2,array3)


            

        
    
    

