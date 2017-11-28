def stars(list):
    for i in range(len(list)):
        print "*"*list[i]
stars([4,6,2,4,7,8,3,21])

def stars2(arr):
    for thing in arr:
        if type(thing) is int:
            print "*"*thing
        elif type(thing) is str:
            print thing[0].lower()*len(thing)
stars2([4,"tom",5,"cvs",12,"john"])