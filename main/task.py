import numpy as np

f1=open("data2angles.txt", 'r')                 # Opening the files
f2=open("data1lenghts.txt", 'r')

movements = f1.read().splitlines()              # Extracting the values from files
lengths = f2.read().splitlines()

for i in range(0, 3):
    lengths[i] = float(lengths[i])              # Converting elements from string to float
    movements[i] = float(movements[i])          

a1 = lengths[0]
a2 = lengths[1]
a3 = lengths[2]

t1 = np.radians(movements[0])
t2 = np.radians(movements[1])
d = movements[2]

cos_t1 = np.cos(t1)
sin_t1 = np.sin(t1)
cos_t2 = np.cos(t2)
sin_t2 = np.sin(t2)

pro01 = np.matrix([                             # proAB = matrix of projection of frame B on frame A
    [1, 0, 0],
    [0, 0, -1],
    [0, 1, 0]
])
rot1 = np.matrix([                              # rot1 = standard rotation matrix in Y axis
    [cos_t1, 0, sin_t1],
    [0, 1, 0],
    [-sin_t1, 0, cos_t1]
])

pro12 = np.matrix([
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0]
])
rot2 = np.matrix([                              # rot2 = standard rotation matrix in Y axis
    [cos_t2, 0, sin_t2],
    [0, 1, 0],
    [-sin_t2, 0, cos_t2]
])

pro23 = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
rot3 = np.matrix([                              # rot3 = identity matrix (no rotation takes place)
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])


rot01 = pro01*rot1                              #
rot12 = pro12*rot2                              # Rotation Matrices
rot23 = pro23*rot3                              #

disp01 = np.matrix([                            #
    [0.0],                                      #
    [0.0],                                      #
    [a1]                                        #
])                                              #
disp12 = np.matrix([                            #   
    [0.0],                                      #   Displacement Vectors
    [0.0],                                      #
    [0.0]                                       #
])                                              #
disp23 = np.matrix([                            #
    [0.0],                                      #
    [0.0],                                      #
    [a2+a3+d]                                   #
])

lastRow = np.matrix([0,0,0,1])                  # last row to be appended to the homogeneous transformation matrices
H01 = np.append(np.append(rot01, disp01, axis=1), lastRow, axis=0)      # 
H12 = np.append(np.append(rot12, disp12, axis=1), lastRow, axis=0)      # Homogeneous Transformation Matrices
H23 = np.append(np.append(rot23, disp23, axis=1), lastRow, axis=0)      #

H03 = H01*H12*H23                               # Final Tranformation Matrix

ans = np.delete(H03, 3, 0)                      # Final 3x4 Matrix
print(ans)
