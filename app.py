## basic monitoring application

import psutil
#gets memory and cpu of server
from flask import Flask, render_template

app = Flask (__name__)

#homepath
@app.route("/")
def index():
    #get cpu
    cpu_percent = psutil.cpu_percent()
    #get memory usage
    mem_percent = psutil.virtual_memory().percent
    Message = None
    
    if cpu_percent > 80 or mem_percent > 80:
        Message = "High CPU or Memory Utilization detected. Please scale up"
        ##cpu and mem percent passed in as variables
    return render_template('index.html', cpu_metric=cpu_percent, mem_metric=mem_percent, message=Message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
    
    
    
    
    
    

 
