import requests
import json

def send_message_to_google_cloud():
    url = "https://us-central1-python-pubsub-firestore.cloudfunctions.net/automation_readings"
    data = {
        'sensorName': 'automation-sensor-001',
        'sensorReference': 'BTC0021345',
        'temperature': 100.0,
        'humidity': 58.0
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(f'response = {response}')

# to show that script is being run as the main module
if __name__ == '__main__':
    send_message_to_google_cloud()
