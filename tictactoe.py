
from pprint import pprint

board=[['[ ]' for i in range(3)]for i in range(3)]

count = 2
num=0
while True:
    row=int(input())
    column = int(input())
    if count%2 == 0:
        board[row][column] = '[X]'
    else:
        board[row][column] = '[O]'
    for i in board:
        print(' '.join(i))
    num+=1
    count+=1
    if num ==9:
        break

