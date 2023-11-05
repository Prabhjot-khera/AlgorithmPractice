string=input('enter a string here: ')
txt=''
for i in range(len(string)):
    if string[i] !=' ':
        txt+=string[i]
txt=txt.lower()
print(txt)
if txt == txt[::-1]:
    print(' Palindrome')
else:
    print('not palindrome')