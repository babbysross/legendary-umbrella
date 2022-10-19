from ast import Global


text = "The number is "
def plusone(number):
    global text
    print(text + str(number))
    return number+1
    

newnumber = plusone(5)
print(text + str(newnumber))