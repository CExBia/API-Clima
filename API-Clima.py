# -*- coding: utf-8 -*-

#Acessa api de clima
from flask import Flask, request, render_template, jsonify
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
    action_js = {"fulfillmentText": "A temperatura é de " + str(temp_c) + "graus",
                     "fulfillmentMessages": [{"name": "projects/teste1-4a3c3/agent/intents/3b7a1380-cce5-4321-b98e-fbb6230e84c1",
                                              "displayName": "Clima", "webhookState": "WEBHOOK_STATE_ENABLED", "priority": 5000,
                                              "isFallback": False, "mlEnabled": True, "mlDisabled": False, "inputContextNames": [],
                                              "events": [], "trainingPhrases": [{}], "action": "temperatura.clima",
                                              "outputContexts": [{}], "resetContexts": False, "parameters": [{}],
                                              "messages": [{"plataform": "google","text": "A temperatura é de " + str(temp_c) + "graus"}],
                                              "defaultResponsePlatforms": [""], "rootFollowupIntentName": True,
                                              "parentFollowupIntentName": "Clima", "followupIntentInfo": [{}]}],
                     "source": "http://tempeclima.heroku.com"}

    return jsonify(action_js)  
    #return render_template('temperatura.html', temp=temp_c)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)  
    #caso não funcione, coloque ", debug=True)". dessa forma app.run(host='0.0.0.0', port=port)
