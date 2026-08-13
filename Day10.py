'''
Sequences --> Srtings,Lists,Tuples,Sets
Mapping --> Dictionary

#Lists --> Collection of heterogenous elements(items)
#Lists -->Indexed,Ordered,Mutable,Heterogenous,we use [] to store the data

marks = [35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)
#Operations : Indexing,slicing,striding,Membership,Merging,Repetition

#Nested Lists --> A list inside another list
'''
names = ['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
'''
print(len(names))
print(names[0])
print(names[3])
print(names[-3])
print(type(names[0]))
print(names[0][:4])

print(names[3])
print(len(names[3]))
print(names[3][2])

#Indexing,slicing -->Mutable
names[2] = 'python'
print(names)
#By indexing if we change the elements,lenght of collection will remain same
names[4] = ['codegnan','PFS','JFS','DA','DS']
print(names)
print(len(names))
print(names[4][0])
print(names[4][0][4::])

names[2:4] = 'Akash','Eramani','sriyansh'
print(names[2:4])
print(names)
#In slicing whatever elements u pass as per the logic lenght keeps on increase

#o/p as follows:
#['codegnan',25,'Akash','java','Eramani','python','DA23']
names[3:6:2] = ['python','Java']
print(names)

#Create a nested list with strings,lists and work on Indexing,slicing,striding
#added advantage if u could add strings functions also to it
#Lists Functions -->append(),insert(),extend(),pop(),remove(),clear()

names = ['codegnan','saketh']
#append() -->inserts single element to the end of the list

names.append('data')
print(names)
#names.append('analysis','agents') #TypeError
#names.append(['analysis','agents'])
print(names)
#append() will always increment the length of list by 1
#print(names[3])
#print(names[3].append('chatgpt')) #it returns None as append is applicable
#on list not print
print(names)

#extend() -->inserts multiple elements to the end of list
names.extend('analysis') #string will be splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,75,24,56])
print(names)
#names.extend(35,45) TypeError -> as only 1 argument to be passed..
#print(names)

#insert(index,object) --> inserts given object before index
names.insert(1,'python')
print(names)
names.insert(0,'java')
print(names)
#names.insert([1:4],['a','b']) #syntaxError
#print(names)
names.insert(-1,'AAA')
print(names)

#pop(),remove(),clear()
#pop() by default last,else given index
print(names.pop())
print(names)
names.pop(2)
print(names)
'''
#remove() we can remove a specific value
names.extend([23,14,15])
print(names)

names.remove(14)
print(names)
names.remove(14) #it raises ValueError
del names[1:3] #del keyword will apply permanent changes
print(names)
names.clear()  #clear() will remove all elements and returns empty list
print(names)

#data = ['codegnan','Eramani', 'python','java'] #input
#output should be as follows
'''
0 : codegnan
1: saketh
2:python
3:java
'''
data = ['codegnan', 'Eramani', 'python', 'java']

for i, value in enumerate(data):
    print(i, ":", value)

print(names.remove(14))

# Nested List
data = [
    "Codegnan",
    ["Python", "Java", "SQL"],
    "Eramani",
    ["Power BI", "Excel", "Tableau"],
    "Data Analyst"
]

print("Original List:")
print(data)


# ---------------- INDEXING ----------------

print("\n--- INDEXING ---")

print(data[0])          # Codegnan
print(data[1])          # ['Python', 'Java', 'SQL']
print(data[1][0])       # Python
print(data[1][2])       # SQL
print(data[3][1])       # Excel


# ---------------- SLICING ----------------

print("\n--- SLICING ---")

print(data[0:3])        # First 3 elements
print(data[1:4])        # Index 1 to 3
print(data[2:])         # Index 2 onwards
print(data[:3])         # First 3 elements


# ---------------- STRIDING ----------------

print("\n--- STRIDING ---")

print(data[::2])        # Every 2nd element
print(data[::3])        # Every 3rd element
print(data[::-1])       # Reverse list


# ---------------- STRING FUNCTIONS ----------------

print("\n--- STRING FUNCTIONS ---")

name = data[0]

print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print(name.startswith("Code"))
print(name.endswith("an"))
print(name.isalpha())
print(name.replace("Codegnan", "Python"))


# String inside nested list
language = data[1][0]

print(language.upper())
print(language.lower())
print(language.startswith("Py"))
print(language.endswith("on"))


# ---------------- APPEND ----------------

print("\n--- APPEND ---")

data.append("Machine Learning")
print(data)


# ---------------- INSERT ----------------

print("\n--- INSERT ---")

data.insert(1, "Statistics")
print(data)


# ---------------- EXTEND ----------------

print("\n--- EXTEND ---")

data.extend(["Deep Learning", "MySQL"])
print(data)


# ---------------- POP ----------------

print("\n--- POP ---")

removed_item = data.pop()
print("Removed:", removed_item)
print(data)


# ---------------- REMOVE ----------------

print("\n--- REMOVE ---")

data.remove("Statistics")
print(data)


# ---------------- CLEAR ----------------

print("\n--- CLEAR ---")

temp = ["Python", "SQL", "Power BI"]
print("Before clear:", temp)

temp.clear()

print("After clear:", temp)















