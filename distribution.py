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
for j in range(10):
    for x in strlist:
        if x not in alphabet:
            strlist.remove(x)
            
print (strlist)

strlen=len(strlist)
final=[]
for a in alphabet:
    letterstrin = ""
    for j in range(10):
        if a in strlist:
            letterstrin = letterstrin + a
            strlist.remove(a)
    final.append(letterstrin)
newfinal = []
for a in final:
    for b in alphabet:
        if b in a:
            newfinal.append(a)
print (newfinal)

for b in range(100):
    gofor = 0
    gofor1 = 1
    while gofor < (len(newfinal)-1):
        x = ""
        print (gofor)
        print (newfinal[gofor])
        print (newfinal[gofor1])
        if len(newfinal[gofor]) < len(newfinal[gofor1]):
            x = newfinal[gofor]
            newfinal[gofor] = newfinal[gofor1]
            newfinal[gofor1] = x
       gofor = gofor + 1
       gofor1 = gofor1 + 1

print (newfinal)


