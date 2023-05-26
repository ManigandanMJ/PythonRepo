import logging
logging.basicConfig(filename = "c:\\logs\\no_idea_log.log",filemode ='w',)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def no_idea():
    log.info("Entered no_idea function")
    n, m = input().split()
    for j in range(len(n)):
        log.info("Receiving values of array")
        arr = list(input())
    log.info("Receiving set A values")
    set_A = set(input().split())
    log.info("Receiving set B values")
    set_B = set(input().split())
    happiness = 0
    for i in arr:
        if i in set_A:
            log.info("set value 1 found")
            happiness += 1
        elif i in set_B:
            log.info("set value B found")
            happiness -= 1
        else:
            happiness == happiness
            print("Happiness : ", happiness)
    return happiness


