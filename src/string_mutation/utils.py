# To change the tuple string to mutable
def mutation(position,new_char):
    old_str = 'abracadabra'
    str_list = list(old_str)
    str_list[int(position)] = new_char
    str_new = ''.join(str_list)
    print(str_new)
    return str_new
