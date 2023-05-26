import numpy
import logging

logging.basicConfig(filename="c:\\logs\\min_max_log.log", filemode='w', )
log = logging.getLogger()
log.setLevel(logging.DEBUG)
def min_max():
    n, m = map(int, input().split())
    log.info("Received row and coloum values")
    array = []

    for i in range(n):
        log.info("Two dimentional array values received")
        array.append(list(map(int, input().split())))

    min_axis = numpy.min(array, axis=1)
    log.warning("Min value received")
    print(numpy.max(min_axis))
    max_axis = numpy.max(min_axis)
    return max_axis
