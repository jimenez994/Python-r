#Assignment: Making Dictionaries
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse","mom", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict = {}
    keys = list1
    values = list2
    if len(list1) < len(list2):
        keys = list2 
        values = list1
    for key in range (0,len(values)):
        new_dict[keys[key]] = values[key]
    return new_dict
new = make_dict(name,favorite_animal)

print new
