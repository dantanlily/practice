#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 15:26:41 2023

@author: dantan
"""
import cpuinfo
from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/cpuinformation')
def cpuinformation():
    cpu_count = psutil.cpu_count()
    #cpu_model = psutil.cpuinfo()[0].get('model name')
    cpu_model=cpuinfo.get_cpu_info()['brand_raw']
    return jsonify({'nr_cpus': cpu_count, 'model_name': cpu_model})

@app.route('/memoinfo')
def memoinfo():
    mem = psutil.virtual_memory()
    total_mb = mem.total // (1024 ** 2)
    used_mb = mem.used // (1024 ** 2)
    free_mb = mem.available // (1024 ** 2)
    return jsonify({'total_mb': total_mb, 'used_mb': used_mb, 'free_mb': free_mb})

if __name__ == '__main__':
    app.run(port=6000)

'''
(base) dantan@Lins-MacBook-Pro ~ % curl http://localhost:5000/cpuinformation
{"model_name":"Apple M2","nr_cpus":8}
(base) dantan@Lins-MacBook-Pro ~ % 
'''
'''
Last login: Sat Mar 25 16:22:17 on ttys001
(base) dantan@Lins-MacBook-Pro ~ % curl http://localhost:6000/cpuinformation
curl http://localhost:6000/memoinfo

{"model_name":"Apple M2","nr_cpus":8}
{"free_mb":297,"total_mb":8192,"used_mb":746}
(base) dantan@Lins-MacBook-Pro ~ % 

'''

