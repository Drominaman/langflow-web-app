from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__, static_folder='.')

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "0524ccb4-770a-4d15-b95f-f6feb55615a0"
FLOW_ID = "375e0f01-52ae-403f-b979-dae4a17e97f2"
import os
APPLICATION_TOKEN = os.getenv("APPLICATION_TOKEN")

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/run_flow', methods=['POST'])
def run_flow():
    data = request.json
    message = data.get('message')

    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{FLOW_ID}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {
        "Authorization": f"Bearer {APPLICATION_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(api_url, json=payload, headers=headers)

    # ADD THIS DEBUGGING LINE
    print("Raw API Response:", response.text)

    try:
        return jsonify(response.json())
    except:
        return jsonify({"error": "Invalid JSON received from API", "details": response.text})


    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{FLOW_ID}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {
        "Authorization": f"Bearer {APPLICATION_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(api_url, json=payload, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

