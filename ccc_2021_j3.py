#Secret Instruction ccc 2021 J3
#ICS4U0-A
#Prabhjot Khera
#662846
#Mr Veera
#17 september 2021

#ALGORITHM
#create a variable to hold the current direction out of the loop so if 00 occurs you have the previous direction stored
#create while loop as you do not know how many iterations 
#get instructions from user and store inside a variable within the loop
#check for condition '99999' is entered as that is when you break the loop 
#create variable to hold current direction 
#find sum of first 2 integers using slicing and int() to turn the string into numbers 
#check if the sum is 0 in which case you display the previous direction 
#check if the sum is even in which case you display right 
#else it will be odd in which case you display the left direction
#set previous direction to current direction 
#output the direction and last 3 digits of instructions(can be done with slicing)

prev_direction=''  
output=[]

while True:
    instructions= input('enter instruction: ')  
    if instructions=='99999':  
        break
    direction=''  
    sum_two=int(instructions[0])+int(instructions[1])  
    if sum_two==0:
        direction=prev_direction   
    elif sum_two%2==0:       
        direction='right'
    else:
        direction='left'    
    prev_direction=direction
    output.append([direction,instructions[2:]])  

for i in output:
    print(' '.join(i))  #learned in shams class

