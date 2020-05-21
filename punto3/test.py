import numpy as np
np_array = np.array((1, 5, 9, 3, 7, 2, 0))
array = np.where(np_array == 12)

if array[0].size:
    print(array[0][0])
else:
    print('Ma no lo encontre')