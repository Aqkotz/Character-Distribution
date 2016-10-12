"""
distribution.py
Author: Andy
Credit: Milo the Almighty Savior of All Existence

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
strin = input("Please enter a string of text (the bigger the better): ")
strin = strin.lower()
strlist=list(strin)
for j in range(100):
    for x in strlist:
        if x not in alphabet:
            strlist.remove(x)
            
print (strlist)
"""
for i in alphabet:
    listname = [" "]
    numval = ""
    for p in strlist:
        if i in strlist:
            numval = numval + i
            strlist.remove(i)
    listname.append(numval)
"""
timcookbutt=len(strlist)
final=[""]
while timcookbutt >=0:
    pouple=0
    while pouple <= len(alphabet):
        if alphabet[pouple] in strlist:
            final.append(alphabet[pouple])
            strlist.remove(alphabet[pouple])
            pouple=pouple+1
    timcookbutt=len(strlist)

listname.remove(" ")
print (listname)