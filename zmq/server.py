# import sys
# import time

# import zmq

# port = sys.argv[1]
# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind(f"tcp://*:{port}")

# while True:
#     message = socket.recv()
#     print(f"Received message: {message}")
#     time.sleep(0.5)
#     message = f"Reply from {port} for message: {message.decode()}"
#     socket.send(message.encode())

import zmq
import random
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:6556")
while True:
    temp = f"temp {random.randint(15, 25)}"
    socket.send(temp.encode())
    volt = f"volt {random.randint(0, 500) / 100}"
    socket.send(volt.encode())
    time.sleep(1)