import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:9900")
socket.setsockopt(zmq.SUBSCRIBE, '')

while True:
    s = socket.recv()
    print s
