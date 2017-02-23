#
# TCP Server
#
from socket import *
from CRC Calculator import crc

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while 1:
    connectionSocket, addr = serverSocket.accept()
    package = connectionSocket.recv(1024)
    data, gen, crc_code = package.split('_')

    check = crc(data, gen, crc_code)

    print ('crc test result: ',check)
    result = int(check)
    if result != 0:
        user_check = 'Error in transmission'
    else:
        user_check = 'successful transmission'



    capitalizedSentence = data.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.send(user_check)

    connectionSocket.close()