import logging
logging.basicConfig(filename = "c:\\logs\\mail_log.log",filemode ='w',)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def validate_mail():
    log.info("Validating mail Id")
    list_mail = []
    print(type(list_mail))
    for i in range(3):
        log.info("Getting Mail ID's for validation")
        s = input("Enter mail Id : ")
        if s.count('@') != 1:
            print("not valid")
        else:
            username, rear = s.split('@')
            if len(username) > 0:
                for t in username:
                    if not (t.isalnum() or t in ['_', '-']):
                        print("not valid")
            else:
                print("not valid")

            if rear.count(".") != 1:
                print("not valid")
            else:
                website, extension = rear.split('.')
                if len(extension) > 3:
                    print("not valid")
                else:
                    for t in extension:
                        if not t.isalpha():
                            print("not valid")

                for t in website:
                    if not t.isalnum():
                        print("not valid")
        list_mail[i] = list_mail.append(s)
        log.warning("Mail Id's valid")
        print("valid",s)
    return print(list_mail)

