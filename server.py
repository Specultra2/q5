# first of all import the socket library
import socket  
import random          
 
# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")           
 

while True:
 

  c, addr = s.accept()    
  print ('Got connection from', addr )
 
  
  x = random.randint(1,999)
  if x == 12:
    message = 'dua belas'
  elif x == 53:
    message = 'lima puluh tiga'
  else:
    message = x

  c.send(bytes(str(message), 'utf8'))

 
  # Close the connection with the client
  c.close()
   
  # Breaking once connection closed
  break