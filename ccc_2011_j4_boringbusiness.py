#ccc 2011 Boring Business
#ICS4U0-A
#Prabhjot Khera
#662846
#Mr Veera
#28 september 2021

import sys #THIS IS HOW I WILL EXIT THE PROGRAM WHEN DANGER IS PRINTED
#A 2 DIMENSIONAL LIST TO HOLD ALL THE CURRENT AND FUTURE DRILLED POINTS
drilled_holes=[[0,-1],[0,-2],[0,-3],[1,-3],[2,-3],[3,-3],[3,-4],[3,-5],[4,-5],[5,-5],[5,-4],[5,-3],[6,-3],[7,-3],[7,-4],[7,-5],[7,-6],[7,-7],[6,-7],[5,-7],[4,-7],[3,-7],[2,-7],[1,-7],[0,-7],[-1,-7],[-1,-6],[-1,-5]]

output=[]
x,y=-1,-5    #THIS IS WHERE THE WELL PLAN WILL CONTINUE FROM EVERYTIME WE TRY TO DRAW A NEW PLAN
while True:  #WHILE LOOP AS WE DO NOT KNOW WHEN THE USER WILL QUIT THE PROGRAM
    point_of_intersection=0  #THIS WILL KEEP TRACK OF IF THE PATH INTERSECTS WITH ANOTHER POINT
    dir_x=0  #VARIABLE TO HOLD SHIFT IN X DIRECTION
    dir_y=0  #VARIABLE TO HOLD SHIFT IN Y DIRECTION
    #GET USER INPUT FOR DRILLING COMMAND
    command= input('enter drilling commands[q-quit, r-right, l-left, u-up, d-down] + integer (e.g. (l 5) means left 5) **type q + integer to terminate: ')
    direction=command[0] #SLICING TO GET THE DIRECTION FROM INPUT
    magnitude=int(command[2:])  #GETTING THE MAGNITUDE OF THE SHIFT FROM USER INPUT
    if direction=='q': # IF INPUT IS q THEN PROGRAM WILL QUIT
        break 
    if direction=='r': #IF RIGHT THEN SHIFT WILL BE BY 1 EACH TIME IN THE POSITIVE DIRECTION
        dir_x = 1
    if direction=='l': #IF LEFT THEN SHIFT WILL BE -1 AS IT WILL MOVE IN NEGATIVE DIRECTION
        dir_x=-1
    if direction=='u': #IF UP THEN Y SHIFT WILL BE 1 IN POSITVE DIRECTION
        dir_y = 1
    if direction=='d': #IF DOWN THEN Y SHIFT WILL BE -1 TO INDICATE NEGATIVE DIRECTION
        dir_y=-1
    for point in range(magnitude):  # WILL ADD THE SHIFT VALUE UNTIL THE MAGNITUDE IS ACCOUNTED FOR
        x+= dir_x # FOR RANGE IN MAGNITUDE IT WILL CONTINUE TO SHIFT THE X CORDINATE BY 1 OR -1
        y+=dir_y  # FOR RANGE IN MAGNITUDE IT WILL CONTINUE TO SHIFT THE Y CORDINATE BY 1 OR -1
        if [x,y] in drilled_holes:
            point_of_intersection+=1  #IF THE CORDINATE THAT IS CURRENTLY BEING DRILLED IS IN DRILLED_HOLES THEN THIS WILL KEEP TRACK
        drilled_holes.append([x,y])   #APPENDING THE CURRENT POINT INTO THE DRILLED_HOLES LIST
    if point_of_intersection>0:
        output.append([str(x),str(y),'DANGER'])  
    else:
        output.append([str(x),str(y),'SAFE'])

for i in output:
    print(' '.join(i))  #shams tehcnique to print the items of a list in a string
    if i[2]=='DANGER':
        sys.exit()





