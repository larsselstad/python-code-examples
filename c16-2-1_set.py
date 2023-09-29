myset = set([4, -8, 9])
print(myset)

myset = set([4, -8, 9, 4])
print(myset)

addset = set();
addset.add(4)
addset.add(-8)
addset.add(9)
addset.add(-8)
print(addset)
print(len(addset))

addset.remove(9)
print(addset)
print(len(addset))