# -*- coding: utf-8 -*-
"""
Central control for the column software

Created on Sat Jan 30 12:24:35 2016

@author: Jonathan
"""

import data_process as dp
import data_server as ds
import serial
import sys

port = 'COM3'
thread_name = "data1"

try:
    ser = serial.Serial(port, 9600) #for Windows
    dp.data_text.append("Serial port opened")
    data_feed = dp.Arduino_Data_Feed(ser)
except:
    dp.data_text.append("Serial port access failed, using random data")
    data_feed = dp.Random_Data_Feed()

try:
    try:
        thread = dp.Data_Collector(thread_name,data_feed,dp.data_text,dp.data_raw)
        thread.start()
        dp.data_text.append("Thread {} started".format(thread_name))
    except:
        dp.data_text.append("Starting thread {} failed".format(thread_name))  
except (KeyboardInterrupt, SystemExit):
    thread.stop()
    sys.exit()

    
@ds.app.route('/_stop', methods= ['GET'])
def stop():
    print("thread stopped remotely")
    thread.stop = True

## START SERVER ##  
if __name__ == '__main__':
    ds.app.run()#host='0.0.0.0')