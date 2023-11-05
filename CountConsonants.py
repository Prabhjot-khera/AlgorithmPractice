not_cons=[  'b', 'c', 'd', 'f', 'g', 'h',  'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

txt=input('Enter text: ')
cons=0
for i in range(len(txt)):
    if txt[i] in not_cons:
        cons+=1
print('the number of consonants in',txt,'is',cons)
