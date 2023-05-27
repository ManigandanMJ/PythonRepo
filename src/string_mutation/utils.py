# To change the tuple string to mutable
import logging
logging.basicConfig(filename = "c:\\logs\\str_mutation_log.log",filemode ='w',)
log = logging.getLogger()
log.setLevel(logging.DEBUG)
def mutation(position,new_char):
    log.info("Entered the funtion")
    old_str = 'abracadabra'
    str_list = list(old_str)
    log.info("changed the position of old string to new char")
    str_list[int(position)] = new_char
    log.info("join funtion used to join te strings")
    str_new = ''.join(str_list)
    print(str_new)
    return str_new
