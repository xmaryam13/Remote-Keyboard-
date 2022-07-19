
import socket
from  threading import Thread


SERVER = None
PORT  = 8000
IP_ADDRESS  = None



def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    
    musicWindow()
    
setup()