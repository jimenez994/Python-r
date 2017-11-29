import random
def coin_toss():
    print "Starting the program..."
    heads = 0
    tails = 0
    attemp = 1
    for i in range (1,5001):
        random_num = random.uniform(0, 1)
        num = round(random_num)
        if num == 1.0:
            heads += 1
            print "Attemp #", attemp, "Throwing a coin... It's a head! ... Got", heads, "head(s) so far and", tails, "tail(s) so far"
            attemp += 1
        if num == 0.0:
            tails += 1
            print "Attemp #", attemp, "Throwing a coin... It's a tails! ... Got", heads, "head(s) so far and", tails, "tail(s) so far"
            attemp += 1
    print"Ending the program, thank you!"
coin_toss()
