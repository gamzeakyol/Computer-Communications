from socket import *
serverName="192.168.0.101"
serverPort=12000

clientSocket=socket(AF_INET,SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

message=raw_input('Input lowercase sentence:')

clientSocket.send(message)
modifiedMessage=clientSocket.recv(1024)

print 'From Server:', modifiedMessage
clientSocket.close()
