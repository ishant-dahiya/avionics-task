# avionics-task

This program reads the contents of the files containing the lengths of joints and their angles (revolute joints) and displacements (prismatic joints) and calculates the Homogeneous Transformation Matrix using that data.

Firstly, the data from the files is read and stored in lists called movements(contains and angles and displacement) and lengths(contains length of joints).

After that, the elements of the lists are stored in different variables to make the code more readable and so that it's easier to access them.

Then, the rotation matrices and displacement vectors for each joint are constructed. The matrices are constructed using numpy library because it's way easier and efficient to do matrix multiplication using numpy.

Finlly, the homogeneous transformation matrices are constructed for each joint and they are multiplied to get the final transformation matrix.

The right-most column of the final transformation matrix shows the coordinates of the end effector.
