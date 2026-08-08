''' 
#write the python code for the user need to find a current number's to get
#exact number
#Input is secreat number = 123
#output should be print currect guess
secret_number = 123

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Correct guess!")
        break
    else:
        print("Wrong guess, try again.")

#write the python code for the OTP verification but maximum attempt is 7
#Input = 1111
#print output as a correct OTP
#when enter wrong pin then print as a wrong pin upto 7 attemts
OTP = 1111
attempts = 0

while attempts < 7:
    guess = int(input("Enter OTP: "))
    attempts += 1

    if guess == OTP:
        print("Correct OTP")
        break
    else:
        print("Wrong OTP")

if attempts == 7 and guess != OTP:
    print("Maximum attempts reached")

#write a python program for when I went for restaurant and I order some food
#Input = pizza,Burger,Fries,coke,sandwich,noodles,biryani
#output give exit after ordering 7 oreder
#and print as how many items ordered = 7   
items = ["pizza", "burger", "fries", "coke", "sandwich", "noodles", "biryani"]

count = 0

while count < 7:
    order = input("Enter your order: ").lower()

    if order in items:
        count += 1
        print("Order placed:", order)
    else:
        print("Item not available")

print("Exit")
print("How many items ordered =", count)
'''
#A player has three chances to win the game
#Input is Cricket
#output should be print as
#Test case1:         #Test case2:           
#output:'you won'   #output:'you lost'      
#chances:2           #chances:0

chances = 3

while chances > 0:
    game = input("Enter the game: ")

    if game == "Cricket":
        print("You won")
        print("Chances:", chances - 1)
        break
    else:
        chances -= 1

if chances == 0:
    print("You lost")
    print("Chances: 0")






























