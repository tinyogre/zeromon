import zmq
import memmon
import json
import datetime
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:9900")

SAMPLE_INTERVAL = 5

dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None

while True:
    socket.send(json.dumps(memmon.sample(), default=dthandler))
    time.sleep(SAMPLE_INTERVAL)
