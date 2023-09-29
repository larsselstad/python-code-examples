plot_title = "Austin's Plant Experiment 23"

# upper case
print('upper()', plot_title.upper())


# lower case
print('lower()', plot_title.lower())


# title case
print('title()', plot_title.title())


# stip to remove whitespace before and after
plot_title_ws = "   Austin's    Plant Experiment 23\n   "
print(plot_title_ws)
print('strip()', plot_title_ws.strip())


# split string into list
print('split()', plot_title.split())
# split by letter t
print("split('t')", plot_title.split('t'))


# join together a list to string
print("' '.join(['One', 'Two', 'Tree'])", ' '.join(['One', 'Two', 'Tree']))


# format string
print('City: {0} has high minus low {1:4.1f}'.format('Seattle', 67.1 - 43.2))
print('City: {} has high minus low {}'.format('Seattle', 67.1 - 43.2))
print('City: {0} {0} {0} has high minus low {1:.0f}'.format('Seattle', 67.1 - 43.2))
