'''
Functions --> Variable length arguments (*args)
          --> keyword Variable lenght arguments (**Kwargs)

Variable lenght arguments -->The number of poisitional arguments are not
limit we can pass any number of arguments,but we need to use the * repres-
-entation,data is stored in tuple.

def sample(*args):
    """simple demo for *args"""
    print(args)
    print(type(args))
sample() #no arguments
sample(1,3,4,5) #any number
sample('codegnan','saketh',23)
details = [24,45,35,65]
sample(details) #passing a collection
sample(*details) #unpacking values from collection

a,b,c = 13,4,'da'
print(a,b,c)
#a,*b,c = 'python','codegnan',23,45,9.0,98
#a,b,*c = 'python','codegnan',23,45,9.0,98
a,b,*c = 34,'codegnan'
print(a)
print(b)
print(c)
c.extend([23,45,6,7])
print(c)

#Task --> We wanted to calculate the sum of given objects using Function
def add(*a):
    """sum of given objects"""
    print(a)
    print(type(a))
    #take output variable as result
    result = 0
    for i in a:
        #print(i)
        result = result + i
    return result
#print(add())
#print(add(12,3,4,5))
#print(add(1,2,3,4,5))
print(add(3,4,5,'poll','dear',4.5))

def add(*a):
    """sum of given objects"""
    print(a)
    print(type(a))
    result = 0
    for i in a:
        #print(i)
       #if type(i) == int or type(i) == float:
        if type(i) in (int,float,complex):
            #print(i)
            result = result + i
        return result
#print(add(3,4,5,'poll','dear',4.5))
b = list(map(int,input("Enter the values").split(',')))
#print(add(*b)) #* is used to unpack values from collection
print(b)
print(*b)
for i in b:
    print(i,end=' ') #same as here

#keyword varible lenght arguments --> we can pass any number of keyword
arguments we use ** represntation,data is stored in dictionary

def details(**Kwargs):
    """Usage of **kwargs demo"""
    print(Kwargs)
    print(type(Kwargs))
details() #returns empty dictioanary
#details(2,3,4,6,) #raises TypeError
details(name="codegnan",place="Hyd",batch="da")
batch = {'number':'da23','place':'hyd'}
details(**batch)
'''
#Now let us include both of them into a function
def sample(*a,**b):
    """Usage of both variable lenght and keyword variable lenght args"""
    result = 0
    for i in a:
        if type(i) in (int,float,complex):
            result = result + i
    #print(result)
    return result
    for key,value in b.items():
        print(f'key is {key}')
        print(f'Value is {value}')
print(sample(2,4,5,'police','codegnan',3.5,
       name="codegnan",
       place="hyd",
       batch="da23"))

#sample(name="codegnan",23,ids=23445) #positional args follows keyword args











































