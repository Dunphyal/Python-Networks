import binascii,sys

def crc(data, gen, crccode='0000'):

    if (crccode)==0:
        crccode = ' '
        for i in range(len(gen)-1):
            crccode = crccode + '0'

    data = data + crccode
    data = list(data)
    gen = list(gen)

    for n in range(len(data) - len(crccode)):
        if data[n] == '1':
            for m in range(len(gen)):
                data[m+n]=str((int(data[m+n])+int(gen[m]))%2)

    return ' '.join(data[-len(crccode):])

