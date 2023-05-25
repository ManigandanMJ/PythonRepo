import numpy
import numpy as np
numpy.set_printoptions(legacy='1.13')

l=list(map(float,input().split()))
array1 = np.array(l)
def floor_fun():
    print(np.floor(array1))
    return np.floor(array1)
def ceil_fun():
    print(np.ceil(array1))
    return np.ceil(array1)
def rint_fun():
    print(np.rint(array1))
    return np.rint(array1)
