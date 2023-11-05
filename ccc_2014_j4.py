#Party Invite ccc 2014 J4



#ALGORITHM
#get user input for number of friends and how many rounds of elimation
#create a list of the numbered friends 
#create a for loop(know how many iterations) for the number of rounds of elimation
#get user input for what multiple is to be used to elimate people from
#use a for loop to get the indexes but make sure  0 is not inclusive so indexes do not get messy 
#check if the index is a multiple of the number the user gave them
#remove all multiples of user inputted number
#remove 0 from the list as its job is done 
#print each item in list as displayed in the output

Friends=eval(input('enter number of friends: '))
rounds=eval(input('enter number of numbers: '))

friends_list=list(range(Friends+1))

for m in range(rounds):
    multiple=int(input("enter multiple: "))
    for index in range(len(friends_list)-1,0,-1):
        if index%multiple==0:
            friends_list.remove(friends_list[index])
   
friends_list.remove(0)
for i in friends_list:
    print(i)
