#!/usr/bin/env python
import subprocess
import re
import json
import time
import datetime
import sys
import os

samples = []

def sample():
    p = subprocess.Popen('ps -eo pid,rss,comm | grep -v RSS', shell=True, stdout=subprocess.PIPE)
    (stdout,stderr) = p.communicate()
    lines = stdout.split('\n')
    
    procs = []
    total = 0
    for l in lines:
        m = re.match(r'\s*(\d+)\s+(\d+)\s+(.*)$', l)
        if m:
            pid = m.group(1)
            mem = int(m.group(2))
            cmd = m.group(3)
            procs.append((pid, mem, cmd))

            total += mem

    procs.sort(key=lambda proc: proc[1])

    s = {'total': total,
         'time': datetime.datetime.now()}
    i = 5
    for p in procs[len(procs) - 5:]:
        s['top' + str(i)] = {'mem': p[1], 'pid': p[0], 'comm': p[2]}
        i -= 1
        
    return s

def loop():
    SAMPLE_INTERVAL=5
    LOG_SIZE = (2 * 60 * 60) / SAMPLE_INTERVAL
#LOG_SIZE = 2

    while True:
        dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
        f = open(os.path.expanduser('~/memlog.json'), 'w')
        samples.append(sample())
        if len(samples) > LOG_SIZE:
            samples = samples[1:] # Dumb stupid slicing, probably
        
        f.write(json.dumps(samples, default=dthandler))
        f.close()
    
        #print json.dumps(sample(), default=dthandler)
        sys.stdout.flush()
        time.sleep(SAMPLE_INTERVAL)
    
#'| awk \'{print $2 "+"}\' > /tmp/foo ; echo "0" >> foo ; xargs < foo | bc')
