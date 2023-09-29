record1 = ['Seattle', 67.1, 43.2]

print('City: ' + record1[0])

print('High minus low: ' + str(record1[1] - record1[2]))


# use append to add to the end of list
record1.append(55.4)
print(record1)


# use pop to get and remove last item
tmp = record1.pop()
print('tmp', tmp)
print(record1)


# use insert to insert value based on index
record1.insert(1, 55.4)
print(record1)