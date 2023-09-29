string1 = "Jane Doe's Plant Experiment"
print(string1)

string2 = 'Calculate a "pseudo" function'
print(string2)

# Bruk trippel quotes for newline chars and spaces
string3 = '''The force, given by:
    F = ma
"matches" expected values.'''
print(string3)

# slicing fungerer på samme måte som med list/tuples
print('string2[12:-9] =', string2[12:-9])

# man kan bare konkatinere strenger med +
string4 = 'Helium'
int1 = 1
# gir feilmeldingen TypeError: can only concatenate str (not "int") to str
# print(string4 + ' is number ' + int1)
print(string4 + ' is number ' + str(int1))

# tekst over flere kodelinjer
text = 'Exp 1 and ' + \
        'Exp 2 are ' + \
        'both finished.'
print(text)