list1 = [0, 1, 2, 3, 4]

print('list1', list1)

# Første tallet i en slice inkluderes, mens det siste eksluderes
print('Slice for å fjerne siste item "list1[0:-1]" = ', list1[0:-1])

print('Slice for å fjerne 1. item og de 2 siste "list1[1:-2]" = ', list1[1:-2])

# Blankt siste tall betyr "resten av lista"
print('Slice for å bare ha de 3 siste itemene "list1[-3:]" = ', list1[-3:])
