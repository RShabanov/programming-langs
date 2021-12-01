# import sys
# import zmq

# context = zmq.Context()
# socket = context.socket(zmq.REQ)

# for port in sys.argv[1:]:
#     socket.connect(f"tcp://127.0.0.1:{port}")

# for i in range(10):
#     socket.send((f"Message {i}").encode())
#     print(socket.recv())

# socket.close()

import zmq
import sys

topic = sys.argv[1]

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, topic.encode())
socket.connect("tcp://127.0.0.1:6556")

for _ in range(10):
    print(socket.recv())