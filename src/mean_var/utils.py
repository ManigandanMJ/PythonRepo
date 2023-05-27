import numpy
import logging
logging.basicConfig(filename = "c:\\logs\\mean_var_log.log",filemode ='w',)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def mean_var():
    log.info("Logged into function")
    n ,m = map(int, input().split())
    l = numpy.array([input().split() for i in range(n)], int)
    log.info("Mean function calculated")
    print(numpy.mean(l, axis = 1))
    log.info("Var function calculated")
    print(numpy.var(l, axis =0 ))
    log.info("Std function calculated")
    print(round(numpy.std(l),11))
    arr = [numpy.mean(l, axis = 1),numpy.var(l, axis =0 ),round(numpy.std(l),11)]
    print(arr)
    return numpy.mean(l, axis = 1)

