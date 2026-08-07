'''  
#write a python program to caluculate the winings of a batmans amd count boundaries,dot bolls and the total score
list = [4,6,1,0,2,4,0,6]
# Input
runs = [4, 6, 1, 0, 2, 4, 0, 6]

total_score = 0
boundaries = 0
dot_balls = 0

for i in runs:
    total_score = total_score + i

    if i == 4 or i == 6:
        boundaries = boundaries + 1

    if i == 0:
        dot_balls = dot_balls + 1

print("Total Score =", total_score)
print("Boundaries =", boundaries)
print("Dot Balls =", dot_balls)

#write a python program to pattern check for phone unlock process must be
#given in maximum 5 attempts
#Input = [4,5,6,3]
#Correct phone unlock pattern
correct_pattern = [4, 5, 6, 3]

attempt = 1
max_attempts = 5

while attempt <= max_attempts:
    print(f"\nAttempt {attempt} of {max_attempts}")

    # Take input as space-separated numbers
    pattern = list(map(int, input("Enter unlock pattern (4 numbers):").split()))

    if pattern == correct_pattern:
        print("Phone Unlocked Successfully!")
        break
    else:
        print("Incorrect Pattern!")
        attempt += 1

if attempt > max_attempts:
    print("\n Phone Locked! Maximum 5 attempts exceeded.")
'''
#write a python program to pattern check for ATM pin check process must be
#given in maximum 3 attempts
#Input = [4,5,6,3]
# ATM PIN Check Process
correct_pin = [4, 5, 6, 3]
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = list(map(int, input("Enter 4-digit PIN (space separated): ").split()))

    if pin == correct_pin:
        print("PIN Correct! Access Granted.")
        break
    else:
        attempts += 1
        print("Incorrect PIN!")

        if attempts < max_attempts:
            print("Attempts left:", max_attempts - attempts)
        else:
            print("Maximum attempts reached. Your ATM card is blocked.")



































    
