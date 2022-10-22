from random import randint

players = ["X", "O"]
squares = {}                        #Init squares dict    
blanks = []

for pos in (                          #init game squares
        "tl", "tm", "tr",
        "ml", "mm", "mr",
        "ll", "lm", "lr"):
    squares.setdefault(pos, " ")

def prtboard():                     #Print game board
    print(  "\n" +
            squares["tl"] + "|" + 
            squares["tm"] + "|" + 
            squares["tr"])
    print("------")
    print(
            squares["ml"] + "|" + 
            squares["mm"] + "|" + 
            squares["mr"])
    print("------")
    print(
            squares["ll"] + "|" + 
            squares["lm"] + "|" + 
            squares["lr"] + "\n")

def getblanks():                    #get blank squares from game board
    for pos in squares:
        if squares[pos] == ' ':
            blanks.append(pos)

print("You're playing Tic Tac Toe!\n")

while True:     #get the player to select X or O, with input validation
    try:
        player = str.upper(input("Do you want to be X or O? "))
        players.index(player)
        print("Cool, you're " + player + ".")
        break
    except ValueError:
        print("Pick either X or O, please\n")
        continue

if player == "X":
    baddie = "O"
elif player == "O":
    baddie = "X"

prtboard()

while True:     #take the first move from the player, with input validation
    try:
        move = input("What is your move? (t, m, l & l, m r) ").lower()  #take input, force lower case
        squares[move] == move                                            #return true/false if input is in the squares dict
    except KeyError:
        print("Pick a valid value, please\n")
    else:
        squares[move] = player  #set selected square to player value (X or O)
        break   #exit loop

getblanks()
baddiemove = randint(0,len(blanks)-1)
squares[blanks[baddiemove]] = baddie


prtboard()