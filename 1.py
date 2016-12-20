import random
#We start with Hangman
mytuple=("ant","cat","dog","sheep","spider")
mylist=[]
#tuple can't be updated
print("Starting the Game: ")
r=random.randint(0,len(mytuple)-1)
secretWord=mytuple[r]
l=len(secretWord)
for i in range(0,l):
    mylist.append("_ ")
print(secretWord)
print(mylist)
str=input("Guess the letter?" )
print(str)
if str in secretWord:
    print("Yay")
else:
    print("Nay")
print("done finally")
