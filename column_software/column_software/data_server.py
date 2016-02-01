# -*- coding: utf-8 -*-
"""
Server module

Created on Sat Jan 30 10:25:21 2016

@author: Jonathan
"""
from flask import Flask, jsonify, render_template, request
import data_process as dp
    
app = Flask(__name__)
#app.debug = True #for debugging THIS BREAKS EVERYTHING AHHHOHGODOHGOD

@app.route('/')
def return_data():
    """answer request for data"""
    return render_template('return_data.html')
    
@app.route('/_update', methods= ['GET'])
def update():
    info=dp.format_data(dp.data_list)
    return jsonify(info=info)