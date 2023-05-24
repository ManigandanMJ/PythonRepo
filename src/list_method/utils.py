def list_methods():
    num = int(input("Enter Number of entries : "))
    list_1 = []
    for i in range(num):
        l = input().split()
        option = l[0]

        if option == 'insert':
            list_1.insert(int(l[1]), int(l[2]))

        elif option == 'print':
            print(list_1)

        elif option == 'remove':
            list_1.remove(int(l[1]))

        elif option == 'append':
            list_1.append(int(l[1]))

        elif option == 'sort':
            list_1.sort()

        elif option == 'pop':
            list_1.pop()

        else:  # reverse
            list_1.reverse()
    return list_1