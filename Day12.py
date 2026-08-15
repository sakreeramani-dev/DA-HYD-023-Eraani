'''
sequences --> strings,Lists,Tuples,set,Frozenset
Mapping -> Dictionary

#Sets --> A set is a Unique Collection of objects,Unordered,Mutable,Hashing
#Unidexed,Unique,Heterogenous
#set(),{}
#a = {}
a = set()
print(type(a))
stud_ids = {123,345,234,567,234}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))
#print(stud_ids[2]) #TypeError
print(234 in stud_ids)
#print(stud_ids * 2)
#print(stud_ids + stud_ids) #Two sets cannot be merged

#data = {12,3,4,5,[12,3,4],'Eramani'}
#print(data) #No lists inside a set (hashing technique) Lists are Mutable

data = {12,3,4,5,6,(12,7,8),'Eramani'}
print(data)
print(len(data))
for i in data:
    print(i)

#Methods on sets -->add(),update(),remove(),discard(),pop()
names = {'Eramani','Akash','kiran','codegnan'}
print(len(names))
names.add('python')
print(names)
#names.add('Eramani','poll')
#print(names)
names.add(('poll','police'))
print(names)
names.add(('pooja','varsha'))
print(names)
da_names = {'mani','akash','sai','sonu'}
#update() we can update multiple elements (set)

names.update(da_names)
print(names)
print(len(da_names))
print(da_names)
da_names.update(names)
print(len(names))
print(len(da_names))'
#remove(),discard(),pop(),clear()
#remove() remove an element from the set (it must be a member)
da_names.remove('sai')
print(da_names)
#da_names.remove('sai') #KeyError
#discard() will remove an element if its present else it ignores
da_names.discard('codegnan')
da_names.pop()
print(da_names)
print(da_names.pop())
print(da_names)
da_names.clear()
print(da_names)
da_names.add('saira')
print(da_names)
da_names.update(['mani','akash'])
print(da_names)
da_names.clear()

#copy() #create a shallow copy of set (independent of each other)
d = da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)

#mathematical operations -->union(),intersection(),difference(),symmetric_d
#issubset(),issuperset(),isdisjoint()
'''
da_23 = {12,23,34,45,23,36}
da_24 = {34,46,47,23}
#print(event)
'''
print(len(event))
#common = da_23.intersection(da_24)
common = da_23 & da_24 #&
print(common)
#print(len(common))

common = da_23.intersection_update(da_24)
print(common) 
print(da_23)

print(da_23)
print(da_24)
#difference() remove common elements and prints rmng elements from first
#step
#diff = da_23.difference(da_24)
#print(diff)
#f = da_23 - da_24
#print(f)
symm = da_23.symmetric_difference(da_24)
print(symm)
h = da_23 ^ da_24
print(h)

#issubset() --> checksfor all elements to be present in other set
da_24.remove(46)
da_24.remove(47)

print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))

#isdisjoint() returns False for sets having common elements
print(da_23.isdisjoint(da_24))
'''
#Lenght of Unique student ids in a class,where user can enter first input
#he should be giving number of student_ids,he will enter student_ids

n = int(input())
student_ids = input().split()
#print(student_ids)
result = set(student_ids)
print(len(result))





















































