'''
Mapping --> Dictionary --> collection of key-values pairs used to store
related data -->JSON,APIs,database,records

dict() --> data = {} -->data = {key : value}
Dictionary is mutable,Indexed through keys,Ordered,Heterogenous
Keys must be Unique
'''
details = {}
print(type(details))

details = {'Id':'CGH4022','Name':'Eramani',
           'Gender':'F','Age':20,
           'Batch':'DA23','place':'Hyd'}
print(details)
print(len(details))

#Access the data from dictionary
#details[0] #keyError

print(details.keys()) #It returns keys from the dictionary
print(details['Id'],details['Name'])
#if key name is not matching / invalid
#print(details['marks']) #KeyError as marks is not present
details['marks'] = []
print(details)
print(type(details['marks']))

details['marks'].append(20)
print(details)

details['marks'].extend([15,20,22,25])
print(details)

#create a key value pair of practise session
details['practise session'] = ('Tuesday','Thusday','Saturday')
print(details.keys())
#Accessing 3rd day marks of student
print(details['marks'][2])
#Accessing 2nd day of practice session
print(details['practise session'][1])
details['MI'] = ('monday','wednesday','Friday')

#operations -->Mutable,indexing through keys,membership
print('wednesday' in details)
print('MI' in details) #returns True as we have MI as key
'''for i in details:
    print(i) #returns keys one by one

#for i in details.keys():
   # print(f'key = {i}')
    print(details[i])

#keys() --> returns keys from the dictionary

for i in details.values(): #returns value from dictionary
    print(i)

for i in details.items():
    print(i)

for key,value in details.items():
    print(f'key is {key}')
    print(f'Value is {value}')

#update()
details.update({'marks':[],
                'practise session':('Tuesday','Thusday','Saturday')})
print(details)
details['marks'].extend([24,25,26,27])
print(details)
marks = list(map(int,input("Enter the marks:").split(',')))
print(marks)
details['marks'].extend(marks)
print(details)
'''
print(details.keys())
print(details.get('Name'))
print(details.get('Branch')) #it returns None a we dont have Branch as key
print(details.keys())

details.setdefault('Branch') #if key is not present it inserts into dict
print(details)
details['Branch'] = 'CSE'
print(details)

print(details.setdefault('Name'))
print(details.keys())

print(details.pop('Branch')) #we need to mention key
print(details.keys())

print(details.popitem()) #remove and return a key, value pair as a 2-tuple
print(details.popitem())

del details['Id']
print(details.keys())

details.clear() #remove all elements from 0
print(details)

#fromkeys()

data = ['Eramani','Akash','data']
b = dict.fromkeys(data) 
print(dict.fromkeys(data)) #creates a dict but value set to None
print(b)
b['Eramani'] = 31
print(b)

#Task Create a dictionary with your personal details,similar to your
#Codegnan profile
personal_details = {
    'name': 'Sakre Eramani',
    'education': 'B.Tech / B.E in Electronics and Communication Engineering',
    'college': 'Vijay Rural Engineering College',
    'graduation_year': 2025,
    'cgpa': 7.0,
    'role': 'Fresher Data Analyst',
    'skills': ['Python', 'SQL', 'Machine Learning', 'Power BI', 'Excel'],
    'tools': ['Jupyter Notebook', 'MySQL', 'VS Code', 'Streamlit'],
    'location': 'Hyderabad',
    'interests': ['Data Analytics', 'Data Science', 'Machine Learning']
}

print(personal_details)









































