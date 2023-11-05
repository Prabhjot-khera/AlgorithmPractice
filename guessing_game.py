from random import*


condition = False
num=randint(1,20)
while condition == False:
    
    guess=int(input('Enter a number between 1 and 20: '))
    if guess==num:
        print('You won!')
        condition = True
    elif guess<num:
        print('Hint: try a higher number')
    elif guess>num:
        print('Hint: try a lower number')