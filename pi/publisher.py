import zmq
from random import randrange
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    x = randrange(1,100000)
    y = randrange(-80,135)
    z = randrange(10, 60)
    #outString = "%i %i %i" % (x,y,z)
    outString = "%i" % y
    socket.send_string(outString)
    print(outString)
    time.sleep(1)
