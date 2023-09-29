import numpy as np

zdata = np.array([0.43, 8.4, 2.1, 3.4, 5.9])
# venstre side: henter ut de 3 siste elementene
# høyre side: erstatter de med de 3 første elementene
zdata[0:3] = zdata[2:]
print(zdata)