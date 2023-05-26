import numpy as np
import logging
logging.basicConfig(filename = "c:\\logs\\linear_alg_log.log",filemode ='w',)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def linear_alg():
    log.info("Entered linear_alg function")
    arr = []
    n = int(input())
    for i in range(n):
        log.info("receiving array value")
        arr.append(list(map(float, input().split())))

    matrix = np.matrix(arr)
    result = np.linalg.det(matrix)
    log.warning("verified linear algebra values")
    print(round(result, 2))
    return round(result, 2)
