from confluent_kafka import Producer
import time
import requests
import os
print("Starting the producer..")
time.sleep(5)

# Getting env variables from docker-compose file
bootstrap_servers = os.environ.get("KAFKA_BOOTSTRAP_SERVERS")
topic = os.environ.get("TOPIC")
limit = os.environ.get("LIMIT")

# Configuration for the Kafka producer
conf = {
    'bootstrap.servers': bootstrap_servers
}
# Wait for the Kafka broker to be reachable and the topic to be available
while True:
    try:
        producer = Producer(conf)
        # Check if the topic is available
        available_topics = producer.list_topics(topic=topic).topics
        if topic in available_topics:
            print(f"Topic '{topic}' is available. Sending message...")
            break
        else:
            print(f"Topic '{topic}' not available yet. Retrying in 5 second...")
            time.sleep(5)
    except Exception as e:
        print(f"Error: {e}. Retrying in 5 second...")
        time.sleep(5)


# Implement Pokemon API
url = f'https://pokeapi.co/api/v2/pokemon?limit={limit}'
response = requests.get(url)
if response.status_code != 200:
    print(f"Couldn't connect to Pokemon API. error code: {response.status_code}")
    exit(5)

# List of pokemons:
data = response.json()['results']

for pokemon in data:
    name_to_send = str(pokemon['name'])
    producer.produce(topic, key='key', value=name_to_send)
    # Wait for any outstanding messages to be delivered and delivery reports to be received
    producer.flush()
    print (f'Sent message: {name_to_send}')
    time.sleep(10)
print("Finished.")