from random import *


print('High Low Game')
print('RULES')
print('Number 1 through 6 are low')
print('Number 8 through 13 are high')
print('Number 7 is neither high or low ')
points=1000
print('you begin with 1000 points')

guesses=0
while points>0:
    risk=int(input('Enter points or risk: '))
    num=randint(1,13)
    predictions=int(input('<1=high,0=low>: '))
    print('Number is',num)
    if (predictions==0 and num<7) or (predictions==1 and num>7):
        print('You win.')
        points+=(risk*2)
    else:
        print('You lose')
        points-=risk
    guesses+=1
    print('You have',points,'points.')
print('it took you',guesses,'guesses')

