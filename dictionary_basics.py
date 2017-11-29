#Assignment: Making and Reading from Dictionaries
def information (dic):
    for some_key, some_value in dic.iteritems():
        print "My" + " " + some_key + " " + "is" + " " + str(some_value)

info = {"name":"Anna","age":"101","country of birth":"United States","favorite language":"Python"}

information(info)
