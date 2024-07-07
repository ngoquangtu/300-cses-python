# Consider an infinite string that consists of all positive integers in increasing order:
# 12345678910111213141516171819202122232425...

# Your task is to process q queries of the form: what is the digit at position k in the string?
# Input
# The first input line has an integer q: the number of queries.
# After this, there are q lines that describe the queries. Each line has an integer k: a 1-indexed position in the string.
# Output
# For each query, print the corresponding digit.
# Constraints

# 1 \le q \le 1000
# 1 \le k \le 10^{18}

# Example
# Input:
# 3
# 7
# 19
# 12

# Output:
# 7
# 4
# 1

def calculate(k):
    length=1
    count=9
    start=1
    while(k>length*count):
        k-=length*count
        length+=1
        count*=10
        start*=10
    number=start +(k-1)//length
    position_number= (k-1)%length
    return str(number)[position_number]


q = int(input().strip())
queries = []
for _ in range(q):
    k = int(input().strip())
    queries.append(k)
results = []
for k in queries:
    results.append(calculate(k))

for result in results:
    print(result)
