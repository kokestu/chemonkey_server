# -*- coding: utf-8 -*-
"""
Data interfacing and processing module

Created on Sat Jan 30 10:27:01 2016

@author: Jonathan
"""

import threading
import time

#initialize data list
data_list = []
#intialize data list lock
data_lock = threading.Lock()

class data_collector(threading.Thread):
    """thread that manages data collection"""

    def __init__ (self, threadName, ser, data):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.ser = ser
        self.data = data
        self.empty = 0
        self.stop = False

    def run(self):
        time.sleep(2)
        self.empty = 320 #calibrate_at_current(self.ser)
        read_value = 0
        prev = 0
        while not self.stop:
            try:
                read_value = int(self.ser.readline().rstrip()[0:3])
            except:
                read_value = prev
            if read_value != prev:
                if read_value - self.empty > -5 :
                    add = "EMPTY   "
                else:
                    add = "FRACTION"
                message = "{}  {}   v={}".format(build_time(), add, read_value)
                data_lock.acquire()
                self.data.append(message)
                data_lock.release()
            prev = read_value
            time.sleep(0.9)
        return
        
class fake_data_collector(threading.Thread):
    """thread that fakes data collection"""

    def __init__ (self, threadName, ser, data):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.ser = ser
        self.data = data
        self.empty = 0
        self.stop = False

    def run(self):
        time.sleep(2)
        while not self.stop:
            self.data.append(time.gmtime().tm_sec)
            time.sleep(0.9)
        return

def build_time():
    """builds a string of the current time"""
    tm = time.gmtime()
    h = "{}".format(tm.tm_hour)
    m = "{}".format(tm.tm_min)
    s = "{}".format(tm.tm_sec)
    if len(h) < 2:
        h = "0"+h
    if len(m) < 2:  
        m = "0"+m
    if len(s) < 2:
        s = "0"+s
    return "[{}:{}:{}]".format(h,m,s)

def calibrate_at_current(ser, n=10):
    """reads n (default 10) values from the serial port and returns their average"""
    values = []
    for i in range(1,10):
        value = int(ser.readline().rstrip()[0:3])
        values.append(value)
        time.sleep(0.1)
    return sum(values)/len(values) #return average
    
def format_data(thing):
    """formats data list into string"""
    data_lock.acquire()
    output = thing[0]
    for x in thing[1:]:
        add = "\n"
        if '\n' in x:
            add = ""
        output = x + add + output
    data_lock.release()
    return output