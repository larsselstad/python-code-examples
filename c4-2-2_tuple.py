# tuple er en liste hvor man ikke kan endre verdiene i lista
tuple1 = (0, 1, 2, 3, 4)

print('tuple1', tuple1)
print(type(tuple1))

# gir feilmeldingen TypeError: 'tuple' object does not support item assignment
# tuple1[1] = 55

# for å endre verdier kan man endre tuple til list
list1 = list(tuple1)

print('list1', list1)
print(type(list1))

list1[1] = 55

print('list1', list1)

# en list kan konverters tilbake til tuple
tuple2 = tuple(list1)

print('tuple2', tuple2)
print(type(tuple2))