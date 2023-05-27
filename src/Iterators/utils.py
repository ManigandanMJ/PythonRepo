from itertools import combinations
import logging
logging.basicConfig(filename = "c:\\logs\\iterators_log.log",filemode ='w',)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def iterables():
    log.info("Entered the iterables function")
    num = int(input())
    letter = input().split()
    k = int(input())
    log.info("Combinations method is used to combine the letters ")
    lets = list(combinations(letter,k))
    count=0
    for i in lets:
        log.info("Verifies if 'a' is in letters")
        if ('a' in i):
            log.warning("counts the iterator if 'a' ")
            count+=1
    print(count/len(lets))
    return count/len(lets)