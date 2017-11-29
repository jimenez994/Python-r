#Names 
#part1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for student in students:
    print student["first_name"] +" "+ student["first_name"]


#part2
users = {
    'Students': [
        {'first_name':  'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}
counter = 1
print "Students"
for student2 in users['Students']:
    name = student2['first_name'].upper()
    last_name = student2['last_name'].upper()
    character_count = len(name) + len(last_name)
    print counter,name + " " + last_name, " - ", character_count
    counter += 1

counter2 = 1
print "Instructors"
for instructor in users['Instructors']:
    name = instructor['first_name'].upper()
    last_name = instructor['last_name'].upper()
    character_count = len(name) + len(last_name)
    print counter2, name + " " + last_name, " - ", character_count
    counter2 += 1


