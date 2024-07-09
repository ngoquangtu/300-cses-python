# Your task is to place eight queens on a chessboard so that no two queens are attacking each other. As an additional challenge, each square is either free or reserved, and you can only place queens on the free squares. However, the reserved squares do not prevent queens from attacking each other.

# How many possible ways are there to place the queens?

# Input
# The input has eight lines, and each of them has eight characters. Each square is either free (.) or reserved (*).

# Output
# Print one integer: the number of ways you can place the queens.

# Example
# Input:

# ........
# ........
# ..*.....
# ........
# ........
# .....**.
# ...*....
# ........
# Output:

# 65

def calculate(s):
    count=0
    board = [[0 for _ in range(8)] for _ in range(8)]
    for i in range (8):
        for j in range (8):
            if s[i * 8 + j] == ".":
                board[i][j]=1
            if s[i * 8 + j] == "*":
                board[i][j]=0
    for j in range (8):
        for i in range(8):
            count=count+1
            if i==j or board[i][j]==0:
                continue
            if 
    print(count)

calculate("..................*..........................**....*............")

