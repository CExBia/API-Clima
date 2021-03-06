#Acessa api de clima
from flask import Flask, request, render_template
import requests

app = Flask(__name__)
@app.route('/temperatura', methods=['POST'])
def temperatura():
    city_name = request.form('q')
    r = requests.get('https://owm.io/data/2.5/weather?q='+city_name+',uk&appid=18db156f5ef1c6bdad1be1c5072fa282')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_c = (temp_k - 273.15)
    
    return render_template('temperatura.html', temp=temp_c)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
