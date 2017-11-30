#Assignment: Find Characters
# input
word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
def find_ch (list):
    new_list = []
    for count in range (0,len(list)):
        if "o" in list[count]:
            new_list.append(list[count])
    print new_list

find_ch(word_list)




