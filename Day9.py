'''
Strings -->CaseConverstions,Searching & Finding, String testing methods,
Replace,Space removal

#Searching,Finding,Replacing,Joining
a = "codegnan"
print(len(a))
print(min(a))
print(max(a))

b = a.index('g') #it returns the index position
print(b)
c = a.index('n') #it returns only the first occurance
print(c)
d = a.index('g') #it returns the next occurance
print(d)
#e = a.index('n',8) #ValueError
#print(e)
#f = a.index('t') #ValueError
#print(f)

S = "Eramani@123"
print(len(S))
print(max(S))
print(min(S))
S = S.index('E')
print(S)

a = "codegnan"
#rindex() --> returns last occurance
b = a.rindex('g')
print(b)
c = a.rindex('n') #here 'n' is occuring at 7th index
print(c)
#d = a.rindex('n',8) #it returns ValueError
#print(d)

#count() -->returns the number of items object is repeating

print('Codegnan'.count('n'))
print('code'.count('w')) #It returns 0 as we dont have 'w' in 'code'
print('Cakshjasaksajs'.count('a'))

#find() --> first occurance but it avoid error returns -1 if substring is
#not found
print('codegnan'.find('r')) #it retuns -1
print('codegnan'.find('n'))

a = "DataAnalysis"
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))

#Replacing,splitting,Joining
#Strings are Immutable
a = 'Codegnan'
#a[4] = 's'
print(a.replace('g','s'))
print(a)
a = a.replace('g','s')
print(a)
print('fghijijijji#ecdcx#cscsdxc#vavav#manan'.replace('#',''))

a = 'code Eramani python'
b = a.split() #by default if we have space it splits
print(b)
print(len(b))
c = 'code,Eramani,python'
d = c.split()
print(d)
e = c.split(',')
print(e)

#join()
a = 'code'
b = 'gnan'
print(a.join(b))
print(b.join(a))
print('$'.join('Eramani'))

#Strings testing methods (boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower().....

a = 'Codegnan123'
print(a.isalnum()) #returns True for alphanumeric strings else False
print(a.isalpha()) #returns True only for alphabets
print(a.isdigit()) #returns True only for digit strings
print('8106429771'.isdigit())
print('2345'.isnumeric()) #this has upper edge(numbers,fractions,romans)
#startswith() --> how its starting
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))

print('codegnan'.islower()) #returns True for all lowercase
print('C0degann'.isupper()) #returns True for all uppercase
print('codegnan python'.istitle())

#space removal --> strip() (removes leading and trailing spaces)
a ='  codegnan  '
print(a.strip())
b = input("Enter the strings:").strip().lower()
print(b)

#Zfill() filling with zeros as per the given numeric string
print('234'.zfill(4))
print('234'.zfill(7))
#center(),ljust(),rjust() -->Alignment of strings (check length and then
#modify the width accordingly)
print('hai'.center(6,'#'))
print('hai'.center(6,'#'))

print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))





















