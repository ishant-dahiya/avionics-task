import math
import numpy as np

f1=open("data2angles.txt", 'r')
f2=open("data1lenghts.txt", 'r')

movements = f1.read().splitlines()
lengths = f2.read().splitlines()

for i in range(0, 3):
    lengths[i] = float(lengths[i])
    movements[i] = float(movements[i])

print(movements)
print(lengths)

a1 = lengths[0]
a2 = lengths[1]
a3 = lengths[2]

t1 = np.radians(movements[0])
t2 = np.radians(movements[1])
d = movements[2]

cost1 = np.cos(t1)
sint1 = np.sin(t1)
cost2 = np.cos(t2)
sint2 = np.sin(t2)

x = np.matrix([[0], [0], [0], [1]])
