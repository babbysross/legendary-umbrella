for i in range(4):
    print(i)

peeps = ["Barry", "Harry", "Garry", "Carrie"]

for i in range(len(peeps)):
    print(i)

bart = range(4)
bort = list(range(4))
print("Bart is '" + str(bart) + "', but Bort is '" + str(bort) + "'")
print(list(range(1,100,2)))

for i in range(len(peeps)):
    print(peeps[i] + " is number " + str(i))

a = "bart"
b = "bort"
print(a + " " + b)
a, b = b, a
print(a + " " + b)