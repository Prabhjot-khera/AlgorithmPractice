#Pg 270 example 12
#ICS4U0-A
#Prabhjot Khera
#662846
#Mr Veera
#28 september 2021

from random import *

board=[['[      ]' for i in range(5)]for i in range(5)]          #create a 2d lists of the rows and columns of the board
prizes=['[ GAME ]','[PUZZLE]','[POSTER]','[ DOLL ]','[ BALL ]']   #list to hold the prizes

count=0
winnings={'[ GAME ]':3,'[PUZZLE]':3,'[POSTER]':3,'[ DOLL ]':3,'[ BALL ]':3}  #USING ONE OF SHAMS LESSONS(DICTIONAIRES) TO HOLD THE COUNT OF EACH PRIZE
while count!=15:   #will add prizes until there are 15 on the board
    row=randint(0,4)
    col=randint(0,4)
    if board[row][col]=='[      ]':
        prize=choice(prizes)
        if winnings[prize]!=0:  #checking to see if 3 of the prizes are already on the board
            board[row][col]=prize    #adding a prize to an empty slot on the board
            count+=1
            winnings[prize]-=1

for i in board:
    print(' '.join(i))   #displaying the game board

winnings={'[ GAME ]':3,'[PUZZLE]':3,'[POSTER]':3,'[ DOLL ]':3,'[ BALL ]':3}   # resetting dictionary as we need all 3 counts of each prize for when pennies are placed

penny_count=0
while penny_count!=10:  #PLACING TEN PENNIES ON THE BOARD
    rows=randint(0,4)
    cols=randint(0,4)
    if board[rows][cols] in prizes:  #CHECKING IF PENNY LANDED ON A PRIZE
        penny_prize=board[rows][cols]
        penny_count+=1
        winnings[penny_prize]-=1        #IF PENNY LANDS ON PRIZE NEEDS TO TAKE AWAY ONE FROM THE COUNT       
        board[rows][cols]='[pennys]'  #REPLACE PRIZE WITH A penny 

    elif board[rows][cols]=='[      ]': 
        board[rows][cols]='[pennys]'
        penny_count+=1

print('this is the board after pennys:')
for i in board:
    print(' '.join(i))

actual_wins=[]
for i in winnings.keys():
    if winnings[i]==0: #LOOKING FOR A PRIZE WHERE ALL NAMES OF IT HAVE A PENNY ON IT
        actual_wins.append(i)

if actual_wins==[]:
    print('you did not win anything')
else:
    print('you have won:', ' '.join(actual_wins))






