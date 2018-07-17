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
    action_js = {"fulfillmentText": "A temperatura é de " + str(temp_c) + " graus",
 "fulfillmentMessages": [{"name": "projects/teste1bia-f1971/agent/intents/a90a3e24-bea5-47aa-be31-2db3818d12a4",
                          "displayName":"Clima", "webhookState": "WEBHOOK_ENABLE", "priority": 3,
                          "isFallback": False, "mlEnabled": True, "mlDisabled": False, "inputContextNames": "",
                          "events": "", "trainingPhrases": ["Qual a temperatura em São Paulo?"],
                          "action": "temperatura.clima", "outputContexts": "", "resetContexts": False,
                          "parameters": "", "messages": "A temperatura é de " + str(temp_c) + " graus",
                          "defaultResponsePlatforms": [5], "rootFollowupIntentName": "", "parentFollowupIntentName": "",
                          "followupIntentInfo": "Informa a  temperatura"}], "source": "http://tempeclima.herokuapp.com/",
                     "payload": {"google": {"expectUserResponse": True,
                                            "richResponse": {"items": [{"simpleResponse": {"textToSpeech": "A temperatura é de " + str(temp_c) + " graus"}}]}},
                                 "facebook": {}, "slack": {}},
                     "outputContexts": [{"name": "projects/${PROJECT_ID}/agent/sessions/${SESSION_ID}/contexts/context name",
                                         "lifespanCount": 5, "parameters": {}}],
                     "followupEventInput": {"name": "","languageCode": "pt-BR","parameters": {}}}

    return jsonify(action_js)  
    #return render_template('temperatura.html', temp=temp_c)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)  
    #caso não funcione, coloque ", debug=True)". dessa forma app.run(host='0.0.0.0', port=port)
