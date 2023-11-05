#ccc 2011 Boring Business


drilled_holes=[[0,-1],[0,-2],[0,-3],[1,-3],[2,-3],[3,-3],[3,-4],[3,-5],[4,-5],[5,-5],[5,-4],[5,-3],[6,-3],[7,-3],[7,-4],[7,-5],[7,-6],[7,-7],[6,-7],[5,-7],[4,-7],[3,-7],[2,-7],[1,-7],[0,-7],[-1,-7],[-1,-6],[-1,-5]]


output=[]
current_point=[-1,-5]
while True:
    prev_point=current_point
    command= input('enter drilling commands(e.g. (r 5) means right 5, type q to terminate: ')
    direction=command[0]
    magnitude=command[2:]
    if direction=='q':
        break 
    if direction=='r':
        count_of_intersections=0
        current_point[0]+=int(magnitude)
        start1 = prev_point[0] 
        end1 = current_point[0]+1
        start2 = prev_point[1]
        end2 = current_point[1]+1
        for x in range(start1, end1):
            for y in range(start2, end2):
                new=[x,y]
                if new in drilled_holes:
                    count_of_intersections+=1
        if count_of_intersections>0:
            output.append([str(current_point[0]),str(current_point[1]), 'DANGER'])
        else:
            output.append([str(current_point[0]),str(current_point[1]), 'SAFE'])
    
    if direction=='l':
        count_of_intersections=0
        current_point[0]-=int(magnitude)
        for x in range(current_point[0], prev_point[0]+1):
            for y in range(prev_point[1], current_point[1]+1):
                new=[x,y]
                if new in drilled_holes:
                    count_of_intersections+=1
        if count_of_intersections>0:
            output.append([str(current_point[0]),str(current_point[1]), 'DANGER'])
        else:
            output.append([str(current_point[0]),str(current_point[1]), 'SAFE'])

    if direction=='d':
        count_of_intersections=0
        current_point[1]-=int(magnitude)
        for x in range(current_point[0], prev_point[0]+1):
            for y in range(current_point[1], prev_point[1]+1):
                new=[x,y]
                print(new)
                if new in drilled_holes:
                    count_of_intersections+=1
        if count_of_intersections>0:
            output.append([str(current_point[0]),str(current_point[1]), 'DANGER'])
        else:
            output.append([str(current_point[0]),str(current_point[1]), 'SAFE'])
    
    if direction=='u':
        count_of_intersections=0
        current_point[1]+=int(magnitude)
        for x in range(current_point[0], prev_point[0]+1):
            for y in range(prev_point[1], current_point[1]+1):
                new=[x,y]
                if new in drilled_holes:
                    count_of_intersections+=1
        if count_of_intersections>0:
            output.append([str(current_point[0]),str(current_point[1]), 'DANGER'])
        else:
            output.append([str(current_point[0]),str(current_point[1]), 'SAFE'])

for i in output:
    print(' '.join(i))



