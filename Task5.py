
1.#Task: Ask the user to enter a sentence. Display the same sentence in several different letter 
#cases.
S = "Data analyst"
print(S)
print(S.upper())
print(S.lower())
print(S.capitalize())
print(S.title())
print(S.swapcase())

2.#Task: Repeatedly ask the user for a username 
#and report which validation rules it passes. Stop 
#when the user enters quit. 

while True:
    username = input("Enter username (or 'quit' to stop): ")

    if username == "quit":
        print("Program stopped.")
        break

    # Check alphanumeric
    if username.isalnum():
        print("Contains only letters and numbers")
    else:
        print("Does not contain only letters and numbers")

    # Check first character
    if username[0].isalpha():
        print("Begins with a letter")
    else:
        print("Does not begin with a letter")

    # Check Python identifier
    if username.isidentifier():
        print("Valid Python identifier")
    else:
        print("Not a valid Python identifier")

    # Check ASCII
    if username.isascii():
        print("Contains only ASCII characters")
    else:
        print("Contains non-ASCII characters")

    print()

 
3.#Task: Collect the names and marks of three 
#students, assign a grade, and display a neatly 
#aligned report. 
print("=" * 40)
print("STUDENT REPORT".center(40))
print("=" * 40)

print(f"{'Name'.ljust(20)}{'Marks'.rjust(10)}{'Grade'.rjust(10)}")

for i in range(3):
    name = input("Enter student name: ")

    marks = float(input("Enter marks: "))

    # Validate marks
    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        continue

    # Determine grade
    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"

    # Display student row
    print(f"{name.ljust(20)}{str(marks).rjust(10)}{grade.rjust(10)}")

4.#Read one line of text,examine each character, and report information about both the 
#characters and the complete line.

text = input("Enter a line of text: ")

letters = 0
digits = 0
spaces = 0
printable = 0
non_printable = 0

for ch in text:
    if ch.isalpha():
        letters += 1

    if ch.isdigit():
        digits += 1

    if ch.isspace():
        spaces += 1

    if ch.isprintable():
        printable += 1
    else:
        non_printable += 1

print("\n----- TEXT REPORT -----")
print("Letters       :", letters)
print("Digits        :", digits)
print("Spaces        :", spaces)
print("Printable     :", printable)
print("Non-printable :", non_printable)
print("Lower case    :", text.islower())
print("Upper case    :", text.isupper())
print("Title case    :", text.istitle())































    
