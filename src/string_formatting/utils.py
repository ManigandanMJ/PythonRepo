def print_formatted(num):
    dec,octal,hexa,binary = [],[],[],[]
    for i in range(1,num+1):
        dec.append(str(i))
        octal.append(oct(i)[2:])
        hexa.append(hex(i)[2:].upper())
        binary.append(bin(i)[2:])
    spc = len(binary[-1])
    for i in range(num):
        print(dec[i].rjust(spc), octal[i].rjust(spc), hexa[i].rjust(spc), binary[i].rjust(spc))
    return dec,octal,hexa,binary


#num = int(input())

