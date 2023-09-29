values = []
for i in range(5):
    values.append(i * 2)
print(values)

# using list comprehension
values = [i * 2 for i in range(5)]
print(values)

# using if in list comprehension
values = [i * 2 for i in range(5) if i > 2]
print(values)