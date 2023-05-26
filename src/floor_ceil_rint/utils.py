import numpy
import numpy as np
import logging

numpy.set_printoptions(legacy='1.13')
logging.basicConfig(filename = "c:\\logs\\floor_log.log",filemode ='w',)
log = logging.getLogger()
log.setLevel(logging.DEBUG)
log.info("Received list values")
l=list(map(float,input().split()))
array1 = np.array(l)
def floor_fun():
    log.info("Floor function value")
    print(np.floor(array1))
    return np.floor(array1)
def ceil_fun():
    log.info("Ceil function value")
    print(np.ceil(array1))
    return np.ceil(array1)
def rint_fun():
    log.info("Rint function value")
    print(np.rint(array1))
    return np.rint(array1)
