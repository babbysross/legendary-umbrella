import copy
                                    #example of how references are used differently between mutable (e.g. lists) and immutable (e.g strings, tuples) values.
def eggs(someparameter):            #define a function with a parameter (this will let you modify global variables that get passed in).
    someparameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)                          #feeding the spam array into the eggs function as the 'someparameter' parameter,
                                    #rather than copy the array into sameparameter, the function just references spam,
                                    #so changes to sameparameter are changes to spam.
print(spam)                         #show that the append function adds to a variable outside its local scope.
cheese = copy.deepcopy(spam)        #deepcopy allows a proper copy of a mutable variable so each copy can be edited
                                    #separately.
cheese.append(4)
print(spam)
print(cheese)