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
    """display data"""
    return render_template('return_data.html')
    
@app.route('/liveplot')
def return_my_flot():
    """display my flot"""
    return render_template('basicflot.html')
    
@app.route('/examples.css')
def return_css():
    """provide stylesheet"""
    return app.send_static_file('examples.css')
    
@app.route('/_update', methods= ['GET'])
def update():
    return jsonify(data_text=dp.format_data(dp.data_text),
                   data_raw=dp.data_raw)

@app.route('/_updatemyflot')
def update_flot():
    return jsonify(data=dp.data_raw[-60:])
    
