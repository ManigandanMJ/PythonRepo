import  logging

logging.basicConfig(filename = "c:\\logs\\calendar_log.log",filemode="w")
log = logging.getLogger()
log.setLevel(logging.DEBUG)
def second_max():
    log.info("Logged into second_max method")
    arr = map(int, input().split())
    max_arr = sorted(set(arr))
    print(max_arr)
    x = list(max_arr)
    log.info("Found second runner up value")
    runner_up = (max_arr[-2])
    print(runner_up)
    return runner_up
