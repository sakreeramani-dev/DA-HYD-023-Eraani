'''
#1.Student Marks Manager

marks = []

#Requirement 1 & 2: Accept three marks and append them
for i in range(3):
    mark = int(input("Enter mark: "))
    marks.append(mark)

print("Original marks:", marks)

#Requirement 3: Insert 90 at the beginning
marks.insert(0, 90)

#Requirement 4: Add 75 and 85 using extend()
marks.extend([75, 85])

#Requirement 5: Check for 75 and remove it
if 75 in marks:
    marks.remove(75)

#Requirement 6: Remove the final mark using pop()
removed_mark = marks.pop()
print("Removed mark:", removed_mark)

#Requirement 7: Display final list and length
print("Final marks:", marks)
print("Number of marks:", len(marks))


#2.
#Number List Analyser

numbers = [20, 10, 30, 20, 40, 20]

#Requirement 1: Sort in ascending order
numbers.sort()
print("Ascending order:", numbers)

#Requirement 2: Reverse to descending order
numbers.reverse()
print("Descending order:", numbers)

#Requirement 3: Ask the user for a number
search_number = int(input("Enter a number to search for: "))

#Requirement 4 & 5: Check whether the number exists
if search_number in numbers:
    print("Number found!")
    print("Count:", numbers.count(search_number))
    print("First index:", numbers.index(search_number))
else:
    print("Number not found.")

# Requirement 6: Numerical summary
print("Smallest value:", min(numbers))
print("Largest value:", max(numbers))
print("Total:", sum(numbers))

#3:Even and Odd Number Separator Scenario: A program must separate a mixed list into even and odd numbers. Starting data: Use the following list. numbers = [10, 15, 20, 25, 30, 35
#Even and Odd Number Separator

numbers = [10, 15, 20, 25, 30, 35]

#Requirement 1: Create two empty lists
even = []
odd = []

#Requirement 2, 3 & 4: Check every number and separate them
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)

#Requirement 5: Slicing
print("First three values:", numbers[:3])
print("Last three values:", numbers[-3:])

#Requirement 6: Create a backup using copy()
backup = numbers.copy()

#Requirement 7: Clear the original list
numbers.clear()

print("Original list after clear():", numbers)
print("Backup list:", backup)
'''
#4: Unique Name Manager Scenario: A class list contains repeated student names and needs to be cleaned. Starting data: Use the following list. names = ["Asha", "Rahul", "Asha", "John", "Rahul"]

#Unique Name Manager

names = ["Asha", "Rahul", "Asha", "John", "Rahul"]

#Requirement 1: Convert list into a set
unique_names = set(names)

#Requirement 2: Add Meera
unique_names.add("Meera")

#Requirement 3: Add Arun and Priya using update()
unique_names.update(["Arun", "Priya"])

#Requirement 4: Check for John and remove him
if "John" in unique_names:
    unique_names.remove("John")

#Requirement 5: Attempt to remove David safely
unique_names.discard("David")

# Requirement 6: Display every unique name using a loop
print("Unique student names:")

for name in unique_names:
    print(name)















