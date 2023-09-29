settings = {'linestyle':'--', 'linewidth': 5.0, 'marker':'*'}

print(settings)
print(settings.keys())
print(settings.values())

for ikey in settings.keys():
    print(ikey, ' : ', settings[ikey])

for ikey in settings:
    print(ikey, ' : ', settings[ikey])

letters = 'abcde'
mydict = {}
for i in range(len(letters)):
    mydict[letters[i]] = i
print(mydict)

print('a' in mydict)
print('z' in mydict)

letters = 'edcba'
reverse_mydict = {}
for i in range(len(letters)):
    reverse_mydict[letters[i]] = i
print(reverse_mydict)

sorted_mydict = sorted(reverse_mydict.keys())
for ikey in sorted_mydict:
    print(ikey, ' : ', reverse_mydict[ikey])