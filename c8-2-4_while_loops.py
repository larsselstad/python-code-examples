precip = [5, 3, 4, 2, 2, 1, 0, 6, 5, 2, 7]

i = 0
while i < len(precip):
    if i == 6:
        break
    elif (i % 2) == 0:
        i += 1
        continue
    else:
        print(precip[i])
        i += 1
    