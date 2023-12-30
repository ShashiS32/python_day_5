import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

numbers = ["0","1","2","3","4","5","6","7","8","9"]

symbols = ["!","@","#","$","%","^","&","*","(",")","-","_","="]

print ("Welcome to Pysword Generator")
lettersinput = int(input("How many letters would you like to have in your password?: "))
numbersinput = int(input("How many numbers would you like to have in your password?: "))
symbolsinput = int(input("How many symbols would you like to have in your password?: "))

passwordlist = []

randomletters = 0
randomnumbers = 0
randomsymbols = 0

for i in range (0, lettersinput ):
  randomletters = random.choice(letters)
  appendletters = passwordlist.append(randomletters)

for n in range (0, numbersinput ):
  randomnumbers = random.choice(numbers)
  appendnumbers = passwordlist.append(randomnumbers)
  
for p in range (0 , symbolsinput ):
  randomsymbols = random.choice(symbols)
  appendsymbols = passwordlist.append(randomsymbols)


random.shuffle(passwordlist)


fianlpass = ""
for characters in passwordlist:
  fianlpass = fianlpass + characters

print (fianlpass)