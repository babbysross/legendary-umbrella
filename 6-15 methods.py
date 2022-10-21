spam = ["bong", "bing", "bang", "bung"]

test = input("Guess what's in the list\n")
try:
    spam.index(str(test))
    print("That's in the list")
except ValueError:
    print("that ain't in the list")

spam.append('moose')
print(spam)
spam.insert(1,"boink")
print(spam)
spam.remove("bang")
print(spam)
spam.sort()
print(spam)
spom = ["a", "Z", "B", "y"]
spom.sort()
print(spom)
spom.sort(key=str.lower)
print(spom)