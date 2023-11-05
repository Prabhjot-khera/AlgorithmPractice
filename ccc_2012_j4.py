#BigBang secrets ccc 2012 J4
#ICS4U0-A
#Prabhjot Khera
#662846
#Mr Veera
#17 september 2021


#ALGORITHM
#Get user input for k value in the shift and the message needing to be decoded
#create a variable to hold the decoded message
#create a for loop to iterate through each character in the message
#get the unicode value of the letter currently being iterated through
#calculate the shift of the letters using the formula s=3p+k
#subtract the shift from unicode value to get the position of the character before encoded
#if its less than 65(lowest unicode value for uppercase letters) then get the difference between the subtracted unicode value and 65 character
#subtract the difference from 91 as 90 represents the last uppercase letter and you need the shift to reycycle through the letters again
#use chr to get character from new unicode value and add to the variable for the new message
#account for the fact that the subtracted value will not be lower than 65 and add the pre-shifted value the new message just like that 
#print the new message 
k_value=int(input())
message=input()
new_message=''

for i in range(len(message)):
    uni_value=ord(message[i])
    shift=3*(i+1)+k_value
    new_uni=uni_value-shift
    if new_uni<65:
        diff=65-new_uni
        new_letter=chr(91-diff)
        new_message+=new_letter
    else:
        new_letter=chr(new_uni)
        new_message+=new_letter

print(new_message)