'''
Copyright 2017- John Bunch and Karl Lawson
Main REEK client to connect all REEKs
'''
import REEK_Netflix
import REEK_Amazon
import REEK_Hulu
import REEK_Starz

print("Choose which Service should be used:")
print("1. Amazon")
print("2. Netflix")
print("3. Hulu")
print("4. Starz")

userInput = int(input())

while userInput < 1 or userInput > 4:
    print("Please enter valid #") 
    userInput = int(input())

if(userInput == 1):
    REEK_Amazon.main()
if(userInput == 2):
    REEK_Netflix.main()
if(userInput == 3):
    REEK_Hulu.main()
if(userInput == 4):
    REEK_Starz.main()
