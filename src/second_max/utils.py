def second_max():
    n = int(input())
    arr = map(int, input().split())
    max_arr = sorted(set(arr))
    print(max_arr)
    x = list(max_arr)
    runner_up = (max_arr[-2])
    print(runner_up)
    return runner_up
