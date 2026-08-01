'''
marks = int(input("Enter the marks (1-100):"))
if marks > 0 and marks <= 100:
    if marks >= 90:
        print("user hs secured Grade A")
    if marks >= 80 and marks <=89:
        print("user hs secured Grade b")
    if marks >= 70 and marks <= 79:
        print("user hs secured Grade c")
    if marks >= 60 and marks <= 69:
        print("user hs secured Grade D")
    if marks >= 60: 
        print("user hs failed,study again")
    
else:
    print("Enter only +ve values greater than 0 and less than 100")
'''
#elif keyword --> if-elif-else
'''
if <condition1>.
    statement(s).....
elif <condition2>.
    statement(s).....
elif <condition3>.
    statement(s).....
    ............
    .........
else:
    statement(s)...
    .........
'''
'''
marks = int(input("Enter the marks (1-100):"))
if marks <= 100:
    print("Entered values should be greater than 1 and less than 100")
elif marks >= 90:
    print("user hs secured Grade A")
elif marks >= 80 and marks <=89:
    print("user hs secured Grade b")
elif marks >= 70 and marks <= 79:
    print("user hs secured Grade c")
elif marks >= 60 and marks <= 69:
    print("user hs secured Grade D")
elif marks >= 60 and marks >=0:
    print("user hs failed,study again")
    
else:
    print("No negative values")

#Task --> Same usecase try with if-elif-else usage in other way
'''
'''
#Voter Eligibility checkcase --> make sure to satisfy all possible condition
#>=18 and 100 -->Access
#<18 --> no of years eligibity should tell
#negative values --> not acceptable

age = int(input("Enter the age:"))
if age>=18 and age <=100:
    print('------ User has Vote Eligibility ------')
    print('------ Access Granter ------')
elif age<18 and age>0:
    print('------ User still need to get Vote Eligibility ------')
    print('------ User need to wait for more',(18-age),'year(s) ------')
else:
    print('------ only +ve values and less than 100 Acceptable ------')
    
#prefer if-elif-else....
'''
'''
#output --> print() -->we pass any values also use sep and end
#output Formatting --> old style formatting (using commas)
#% usage (%f,%d),.format() usage,fsting natation
a,b = 7,9
print(a)
print(b)
print(a,b)
name = "Codegnan";batch = "DataAnalysis"
print(name,batch)
print(name,batch,sep=',')
print(name,batch,sep='---------->')
#end='\n',\t -->tab space
print(name,batch,end='\t')
print(name,batch,end = '')
print("Hyderabad")
'''
name='Codegnan';age=7;batch='DA-023';place='Hyderabad'
'''
print(batch,'is in', name)
print(name,'is in', place,'age is',age,'years')
#old style formatting --> %d -->integer ,%s---->string,%f-->float
salary = 24253.256
print("His salary is %d"%(salary))
print("His salary is %f"%(salary))
print("His salary is %.1f"%(salary)) #%.if --> rounding to 1 decimal
'''
#.format() usage
print("{} is in {}".format(name,place)) #order matters

#fstring usage (more recommended)
print(f'{name} is in {place}')





























