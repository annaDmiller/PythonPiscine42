from array2D import slice_me
import numpy as np

family = [  [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]]

print(slice_me(family, 0, 4))
print(slice_me(family, 2, -2))
