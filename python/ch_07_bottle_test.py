# WS added CPU temp

from bottle import route, run, template
from datetime import datetime
import os

def get_temp(): # WS added
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cpu_temp_str = dev.read()[5:-3] # top and tail string
    cpu_temp_C   = float(cpu_temp_str)
    cpu_temp_F   = cpu_temp_C * 9/5 + 32.0
    return cpu_temp_C, cpu_temp_F

@route('/')
def index(name='time'):
    dt     = datetime.now()
    time   = "{:%Y-%m-%d %H:%M:%S}".format(dt)
    tc, tf = get_temp()
    return template('<b>time: {{t}}, cpu temp: {{tc}} deg C, {{tf}} deg F</b>',
                    t=time, tc=tc, tf=tf)

run(host='0.0.0.0', port=80)
