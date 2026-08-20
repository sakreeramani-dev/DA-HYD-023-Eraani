'''
Functions -->Arguments Usage (Variable lenght arguments)
          --> Keyword variable lenth arguments (**kwargs)
Exception Handling / Scope of variables / Built-in functions

Exception handling --> It is a mechanism that helps to respond or make the flow
of execution in normal way,without this error will occur and disrup the flow of
program

common Executions --> valueError,TypeError,IndexError,AttributeError,
ZeroDivisionError...

Synrax:

try:
   #code that will cause the exception
except Exception as e:
   #code will catch the exception
finally:
   #runs irrespective of try/except...


#basic Exception handling
try:
    #a = 10
    a = int(input("Enter the value:"))
    result = (10,2,5,6,7)/a
    print(result)
#except Exception as e:
    #print(e) #It return the message of error
except ValueError:
    print(f'Invalid entry enter only integer values')
except ZeroDivisionError:
    print(f'Division by Zero is not possible')
except NameError:
    print(f'Check the name of variable properly')


a = int(input("Enter the value:"))
result = [10,20,30,40,50]
print(a[50])

#similarly if we want to check other Errors --> IndexError, AttributeError

try:
    a = [10,20,30,40]
    print(a[5])
#except Exception as e:
    #print(e)
except IndexError:
    print(f'Check the length of list properly and access elements')
    

def sample(*a,**b):
    """Usage of both variable lenght and keyword variable lenght args"""
    result = 0
    for i in a:
        if type(i) in (int,float,complex):
            result = result + i
    #print(result)
    #return result
    for key,value in b.items():

try:
    a = [10,20,30]
    a.append(24)
    print(a[5])
except (IndexError,AttributeError) as e:
    print(e)
    a = list(map(int,input("Enter").split(',')))
    print(a)

#BMI --> bmi = (weight) / ((height)**2)
#Feet --> 12 inches --> 1 inch -> 2.54cm
while True:
    try:
        weight = int(input("Enter the weight in kgs:"))
        height = float(input("Enter the height in metres:"))
        #write my logical condition
        if weight > 0 and height > 0:
            #break #stops the flow of executuion of progaram
            #continue
            #pass
        else:
            print("Make sure to enter only correct values")
    except ValueError:
        print(f'Make sure to enter weight as integer only,height also as number')
bmi = ((weight) / (height)**2)
print(bmi)

#Use Exception Handling along with Jumping Statement in Functions BMI Task

#scope of Varaibles --> scope is basically the region/area where it is
#accesible
#Local scope,Global Scope
#Global keyword,Enclosing Scope(Nested Functions nonlocal Keyword)
'''
#Local Scope -->variable defined inside the function accessible inside
'''
def display():
    """usage of Local Scope"""
    name = "Codegnan" #Local variable
    print(name)
display()
#print(name) #it raises nameerror

#Global Scope(variable) -->Defined outside and can be accessible anywhere
#In the script
place = "Hyderabad"
def display():
    """Usage of Local&Global Scope"""
    name = "Codegnan"
    print(name)
    print(f'{name} is in {place}')
display()
print(place)

#Modifying global variable inside the function and accessible outside the function
count = 20
def data():
    """Usage of global Keyword"""
    global count
    count = count + 5
    print(f'Value inside function is {count}')
data()
print(f'value outside function is {count}')

#Local variable has high priority over global variable
count = 20
def data():
    """prority of local vs global variable"""
    count = 5 #local variable
    count = count + 5
    print(f'Value inside function is {count}')
data()
print(f'value outside function is {count}')

#Enclosing Scope (nonlocal keyword)

def outer():
    """Outer function with local variable"""
    count = 5
    def inner():
        """Nested Function"""
        count = count + 10
        print(f'value inside is {count}')
    inner()
    print(f'value outside is {count}')
outer()

#Built-in functions -->variables Builtinscope
len = 56
print(len+4)


print(len('Codegnan')) #TypeError 
'''








































    
