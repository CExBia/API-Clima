# -*- coding: utf-8 -*-

#Acessa api de clima
from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__, template_folder='templates')
@app.route('/temperatura', methods=['POST'])
def temperatura():
    city_name = request.form['city']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&APPID=18db156f5ef1c6bdad1be1c5072fa282')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_c = int(temp_k - 273.15)
    
    return render_template('temperatura.html', temp=temp_c)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)  
    #caso não funcione, coloque ", debug=True)". dessa forma app.run(host='0.0.0.0', port=port)
