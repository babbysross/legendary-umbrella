spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue    #this continues at 3
        #break      this would kill the program at 3
    print ("Spam is equal to " + str(spam) + "\n")