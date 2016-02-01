# -*- coding: utf-8 -*-
"""
Central control for the column software

Created on Sat Jan 30 12:24:35 2016

@author: Jonathan
"""

import data_process as dp
import data_server as ds
import serial

port = 'COM3'
thread_name = "data1"

try:
    ser = serial.Serial(port, 9600) #for Windows
    dp.data_list.append("serial port opened")
except:
    dp.data_list.append("Arduino unavailable, serial port access failed")

try:
    thread = dp.data_collector(thread_name,ser,dp.data_list)
    thread.start()
    dp.data_list.append("thread {} started".format(thread_name))
except:
    dp.data_list.append("starting thread {} failed".format(thread_name))
    
@ds.app.route('/_stop', methods= ['GET'])
def stop():
    print "hello"
    thread.stop = True

## START SERVER ##  
if __name__ == '__main__':
    ds.app.run(host='0.0.0.0')