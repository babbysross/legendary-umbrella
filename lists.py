#ATBSWP Section 6-13
list = ['cat', 'rat', 'bat', 'gat']
print(list[0] + " with a " + list[3])
list2 = [['cat', 'rat', 'bat', 'gat'],[10,20,30]]
list2[0][2]='spat'
print(list2[0][2] + " " + str(list2[1][:2]))
print(list2[0][0:])
print(len(list2))
print('rat' in list2)
del list2[0][1]
print(list2[0][0:])
print(len(list2))
print('rat' not in list2)