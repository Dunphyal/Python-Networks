#
# TCP Client
#

from socket import *
from CRC Calculator import crc

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

sentence = input('Input lowercase sentence:')
generator = input('Input generator:')
crc_code = crc(sentence, generator)

package = sentence + '_' + generator + '_' + crc_code
clientSocket.send(package.encode('utf-8'))
modifiedSentence = clientSocket.recv(1024)
print ('From Server: ', modifiedSentence)

clientSocket.close()
