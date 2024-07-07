# Given a string, your task is to generate all different strings that can be created using its characters.
# Input
# The only input line has a string of length n. Each character is between a–z.
# Output
# First print an integer k: the number of strings. Then print k lines: the strings in alphabetical order.
# Constraints

# 1<=n<=8

# Example
# Input:
# aabac
# Output:
# 20
# aaabc
# aaacb
# aabac
# aabca
# aacab
# aacba
# abaac
# abaca
# abcaa
# acaab
# acaba
# acbaa
# baaac
# baaca
# bacaa
# bcaaa
# caaab
# caaba
# cabaa
# cbaaa


def calculate(current,remaining,result):
    if len(remaining) ==0:
        result.add(current)
        return

    for i in range(len(remaining)):
        calculate(current+remaining[i],remaining[:i]+remaining[i+1:],result)

def generate_all_string(s):
    result=set()
    calculate("",s,result)
    result=sorted(result)
    print(len(result))
    for i in result:
        print(i)
s=str(input().strip())
generate_all_string(s)

