from random import randint
from os import system, name

players = ["X", "O"]
squares = {}                                    #init squares dict    
blanks = []                                     #init blanks list
win = [ ["tl", "tm", "tr"], ["ml", "mm", "mr"], #Win scenarios
        ["ll", "lm", "lr"], ["tl", "ml", "ll"], 
        ["tm", "mm", "lm"], ["tr", "mr", "lr"], 
        ["tl", "mm", "lr"], ["tr", "mm", "ll"]]

for pos in (                                    #init game squares
        "tl", "tm", "tr",
        "ml", "mm", "mr",
        "ll", "lm", "lr"):
    squares.setdefault(pos, " ")

def prtboard():                                 #Print game board
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

def getblanks():                                #get blank squares from game board
    for pos in squares:
        if squares[pos] == ' ':
            blanks.append(pos)

def clear():
    system('cls' if name=='nt' else 'clear')
    print("You're playing Tic Tac Toe!\n")
    return("   ")

clear()
while True:     #get the player to select X or O, with input validation
    try:
        player = str.upper(input("Do you want to be X or O? "))
        players.index(player)
        print("Cool, you're " + player + ".")
        if player == "X":
            baddie = "O"
        elif player == "O":
            baddie = "X"
        break
    except ValueError:
        clear()
        print("Pick either X or O, please\n")
        continue

while True:     #take the first move from the player, with input validation
    clear()
    print("You're playing Tic Tac Toe! You are " + player + ".\n")
    prtboard()
    try:
        move = input("What is your move? (t, m, l & l, m r) ").lower()  #take input, force lower case
        squares[move] == move                                            #return true/false if input is in the squares dict
    except KeyError:
        print("Pick a valid value, please\n")
    else:
        if squares[move] == " ":        #check selected space is blank
            squares[move] = player      #update selected space with X or O
        else:
            print("That space is taken")
            continue


getblanks()
baddiemove = randint(0,len(blanks)-1)
squares[blanks[baddiemove]] = baddie

