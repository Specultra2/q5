# Import socket module
import socket     
from num2words import num2words       
 
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 12345               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
# receive data from the server and decoding to get the string.
x = int(s.recv(1024))
print (num2words(x , lang='id'))
# close the connection
s.close()    
