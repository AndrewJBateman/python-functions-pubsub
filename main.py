import json
import os
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
PROJECT_ID = os.getenv('python-pubsub-firestore')


def automation_readings(request):
    data = request.data

    if data is None:
        print('request.data is empty')
        return ('request.data is empty', 400)

    print(f'request data: {data}')

    data_json = json.loads(data)
    print(f'json = {data_json}')

    sensor_name = data_json['sensorName']
    sensor_reference = data_json['sensorReference']
    temperature = data_json['temperature']
    humidity = data_json['humidity']

    print(f'sensor_name = {sensor_name}')
    print(f'sensor_reference = {sensor_reference}')
    print(f'temperature = {temperature}')
    print(f'humidity = {humidity}')

    # move data to Pubsub
    topic_path = 'projects/python-pubsub-firestore/topics/factory-automation'

    message_json = json.dumps({
        'data': {'message': 'automation sensor readings'},
        'readings': {
            'sensorName': sensor_name,
            'sensorReference': sensor_reference,
            'temperature': temperature,
            'humidity': humidity
        }
    })
    message_bytes = message_json.encode('utf-8')

    try:
        publish_future = publisher.publish(topic_path, data=message_bytes)
        publish_future.result() # verify that the publish succeeded
    except Exception as e:
        print(e)
        return (e, 500)

    return ('Message received and published to Pubsub', 200)
