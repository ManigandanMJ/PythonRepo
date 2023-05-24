def list_methods():
    N = int(input())
    arr = []
    for i in range(N):
        line = input().split()
        command = line[0]

        if command == 'insert':
            arr.insert(int(line[1]), int(line[2]))

        elif command == 'print':
            print(arr)

        elif command == 'remove':
            arr.remove(int(line[1]))

        elif command == 'append':
            arr.append(int(line[1]))

        elif command == 'sort':
            arr.sort()

        elif command == 'pop':
            arr.pop()

        else:  # reverse
            arr.reverse()
    return arr