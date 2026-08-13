'''
Lists,Tuples..

#List --> Mutable,ordered,Heterogenous
#index(),count(),copy(),sort(),reverse()
details = ['codegnan',7,2018,'Hyderabad']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,20,40,23])
print(details.index(20))
print(details.index(20,6))
#print(details.index('python')) #valueError

print(details.count(21))
print(details.count('python')) #it returns 0 as we dont have it

data = ['codegnan','Eramani','python','java'] #input
#output should be as follows

0 : codegnan
1 : Eramani
2 : python
3 : java

for obj in data:
    print(data.index(obj),':',obj)

for obj in range(len(data)):
    print(obj,':',data[obj])
'
#copy() -->shallow copy of the given collection

new = data.copy()
print(new)
print(type(new))
print(len(data))

new[2] ='GenAI'
print(new)
print(data)

data.append('Eramani')
print(new)
print(data)

data.remove('Eramani')
print(new)
print(data)

data.extend('python')
print(new)
print(data)

data = [1,4,5,[21,34,45],23]
print(data)
new = data.copy()
print(new)

new[3][2] = 'Agents'
#whenever we make changes in nested list original will
#also be effected
print(new)
print(data)

new[1] = 'python'
print(new)
print(data)

marks = [14,24,-45,27,35]
print(marks)
marks.sort()
#print(marks)
#print(marks) #returns in ascending order
#marks.sort(reverse = True) #returs in desending order
#print(marks)
marks.insert(20,'python')
#marks.sort()
#revrse() --> returns in reverse order
marks.reverse()
print(marks)
print(marks[::-1])
#type(),len(),max(),min(),print()

print(sorted('codegnan')) #returns List ascending order
#print(sorted(['code','23',34,45])) #raises Error

#Tuples --> Tuples are Indexes,ordered,Heterogenous,Immutable collection
#dimensions,coordinates,database records,we prefer () for tuple notation

a = ()
print(type(a))
print(len(a))

dimensions = 1.5,2.5
print(dimensions)
print(type(dimensions))
#operations -->Indexing,Slicing,striding,Membership,merging,Repetition
courses = ('PFS','ASD',('DA','DS'),'AgenticAI',[100,6,6])
print(courses)
print(len(courses))

print(courses[-2][-2:])
#courses[2] = 23 Tuples are Immutable
courses [-1].append('codegnan') #we can make any modifications inside list
print(courses)

#create a Nested tuple as above and work on slicing,Striding and list function
print('PFS' in courses)
d = courses * 2
print(d)
e = courses + (2,3,4,5) #merging
print(e)

#Tuples Immutable --> count(),index()
print(courses.index('AgenticAI'))
print(courses.count('Agents'))

#print(courses.sort()) #AttributeError -->sort() is in Lists not in Tuples

print(sorted(courses[-1]))
#print(sorted(courses)) #as we have mixed type

#TypeCasting
d = tuple(sorted((23,15,2,87,90)))
print(d)

#accept group of integers space separated
a,b = map(int,input("Enter tha values").split())
print(a,b)

a = tuple(map(int,input("Enter the values").split(',')))
print('a')
print('9+4')
#eval() function can take any kind of input
print(eval('9+4'))

a = eval(input("Enter a list"))
print(a)
print(type(a))
'''
#Task: Take a user input as string,do this in two ways..
'''
1) give the count of each repeating character
Test case 1: programming

r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2)
r is repeating 2 times
index = [1,4]
g is repeating 2 times
index = [3,10]
r is repeating 2 times
index = [6,7]
'''
#1)Count each repeating character
text = input("Enter a string: ")

for char in text:
    if text.count(char) > 1:
        # Print only once for each character
        if text.index(char) == text.find(char):
            print(char, "is repeating", text.count(char), "times")

text = input("Enter a string: ")

for char in text:
    if text.count(char) > 1:
        # Print only when we reach the first occurrence
        if text.index(char) == text.find(char):
            indexes = []

            for i in range(len(text)):
                if text[i] == char:
                    indexes.append(i)

            print(char, "is repeating", len(indexes), "times")
            print("index =", indexes)


































