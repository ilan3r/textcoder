'''
name: cse1210.py
purpose: encrypt / decrypt code from a txt file (default code.txt)

'''
import random

#user instructions
print('Before starting, make sure the text you want to decrypt or encrypt is saved in a .txt file, and the file is closed')


print('')
print('')

# input, return d or e
while True:
    den = input('choose whether you would like to decrypt (type [d] and hit enter), or encrypt (type [e] and hit enter), or quit (type [quit] and hit enter): ')
    if den == 'd':
        den = 'd'
        break
    if den == 'e':
        den = 'e'
        break
    if den == 'quit':
        quit()
    else:
        continue

print('')
print('')

# user instructions
print('next, choose a key. if you are encrypting, choose any integer, but keep note of it because you will need it to decrypt')
print('if you are decrypting, make sure you have the correct integer')


#get the seed from the user
while True:
    key = input('enter any negative or positive, whole number or decimal integer: ')
    try:
        float(key)
        break
    except:
        continue



#ask the user for the filename
while True:
    filename = input('enter a filename of a txt file you have that exists with your text (default code.txt): ')
    if filename =='':
        filename = 'code.txt'
        # default is code.txt
    else:
        filename = filename

# make sure the file exists
    try:
        fh = open(filename, 'r')
        print('file exists, starting...')
        break
    except:
        print('could not find .txt file')
        continue

#first open the file to read it
fh = open(filename, 'r')
lst = []
for char in fh.read():
    lst.append(ord(char))
length = len(lst)
# left with a list of the ord value of each character

random.seed(key)

# add random integer if encrypting
if den == 'e':
    for val in range(length):
        r1 = random.randint(0, 4)
        if lst[val] == 10:  # if newline, do not change
            continue
        lst[val] = lst[val] + r1

# subtract random integer if decrypting
if den == 'd':
    for val in range(length):
        r2 = random.randint(0, 4)
        if lst[val] == 10:  #if newline, do not change
            continue
        lst[val] = lst[val] - r2

# convert all the ASCII values in the list to characters
for newval in range(length):
    lst[newval] = chr(lst[newval])


# open the file and update it with the new characters
fh = open(filename, 'w')
for newchar in lst:
    fh.write(newchar)
fh.close()


# based on encrypted or decrypted, tell the user it was successful
if den == 'e':
    print('SUCCESS! - you can now open the encrypted .txt file!')

if den == 'd':
     print('SUCCESS! - you can now open the decrypted .txt file!')

print('Finished')
