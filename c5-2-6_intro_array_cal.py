import numpy as np

ydata = np.array([2.54, 4.1, 1.21, 3.9, 4])
print('ydata', ydata)
print('ydata is type', type(ydata))

# mean gir gjennomsnitt av ydata
ymean = np.mean(ydata)

print('ymean is type', type(ymean))
print('ymean', ymean)

# mapper hvert item i ydata om til verdi - ymean
ydata_dev = ydata - ymean

print('ydata_dev is type', type(ydata_dev))
print('ydata_dev', ydata_dev)