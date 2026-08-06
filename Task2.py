'''
#If their Ecommerce website is present then calculate the sum of four products cost is how much
products = [1200,1500,1600,1800]

products = list(map(int,input().split(',')))
total = 0
for i in products:
    total = total + i
print('total')

#write a python code to create a password using upper case,lowercase,digits and special character

password = input()
upper_case = 0
lower_case = 0
upper_case = 0
digit = 0
special_character = 0

for char in password:
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'Z':
        lower_case += h
    elif 'o' <= ch <= 'q':
        digit += 1
    else:
        special_case += 1 
print("upper_case:",upper_case)
print("lower_case:",lower_case)
print("digit:",digit)
print("special_character:",special_character)

#To write a mail which is input is in below mentioned and the output is gmail.com,amazon.com
#Input = Eramani@gmail.com
#Input = sudha@amazon.in
email = input().split()
for mail in email:
    print(mail.split('@')[1])

#Input = ["salaar","Bahubali","KGF"]
#output =1.salaar
#2.Bahubali
#3.KGF
movies = ["Salaar", "Bahubali", "KGF"]

for i in range(len(movies)):
    print(i + 1, ".", movies[i], sep="")

print("movies")
'''






























