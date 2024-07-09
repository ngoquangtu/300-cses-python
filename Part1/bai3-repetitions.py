# You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
# Input
# The only input line contains a string of n characters.
# Output
# Print one integer: the length of the longest repetition.
# Constraints

# 1 \le n \le 10^6

# Example
# Input:
# ATTCGGGA

# Output:
# 3

def calculate(s):
    char_array= list(s)
    n=len(char_array)
    max_count=1
    count=1
    for i in range (n-1):
      if char_array[i]== char_array[i+1]:
        count=count+1
        if(max_count<count):
          max_count=count
      else :
        count=1
    return max_count
n = str(input().strip())
print(calculate(n))
