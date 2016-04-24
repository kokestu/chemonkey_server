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
    thread = dp.data_collector(thread_name,ser,dp.data_list)
except:
    dp.data_list.append("Arduino unavailable, serial port access failed. Using fake data.")
    thread = dp.fake_data_collector(thread_name,None,dp.data_list)

try:
    thread.start()
    dp.data_list.append("thread {} started".format(thread_name))
except:
    dp.data_list.append("Starting thread {} failed".format(thread_name))
    
@ds.app.route('/_stop', methods= ['GET'])
def stop():
    print("thread stopped remotely")
    thread.stop = True

## START SERVER ##  
if __name__ == '__main__':
    ds.app.run(host='0.0.0.0')