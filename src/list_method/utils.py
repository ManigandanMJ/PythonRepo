import logging
logging.basicConfig(filename = "c:\\logs\\condition_log.log",filemode ='w',)
log = logging.getLogger()
log.setLevel(logging.DEBUG)
def list_methods():
    log.info("def funtion started")
    num = int(input("Enter Number of entries : "))
    list_1 = []
    log.info("Iterating for loops")
    for i in range(num):
        l = input().split()
        option = l[0]
        log.info("Inserted list value")
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