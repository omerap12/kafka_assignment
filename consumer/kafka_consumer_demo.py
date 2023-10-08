from confluent_kafka import Consumer, KafkaError
import time
import os
print("Start consumer")
time.sleep(5)

# Getting env variables from docker-compose file
bootstrap_servers = os.environ.get("KAFKA_BOOTSTRAP_SERVERS")
topic = os.environ.get("TOPIC")

# Configuration for the Kafka consumer
conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'my-consumer-group', # random consumer group
    'auto.offset.reset': 'earliest'  # Start reading the topic from the beginning if no offset is stored
}

# Wait for the Kafka broker to be reachable and the topic to be available
while True:
    try:
        consumer = Consumer(conf)
        # Check if the topic is available
        available_topics = consumer.list_topics().topics
        if topic in available_topics:
            print(f"Topic '{topic}' is available. Consuming messages...")
            break
        else:
            print(f"Topic '{topic}' not available yet. Retrying in 5 second...")
            time.sleep(5)
    except Exception as e:
        print(f"Error: {e}. Retrying in 1 second...")
        time.sleep(1)

# Subscribe to the Kafka topic
consumer.subscribe([topic])

# Poll for messages
while True:
    msg = consumer.poll(1.0)  # 1-second timeout for polling messages

    if msg is None:
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            # End of partition event - not an error
            continue
        else:
            # Handle other errors
            print(msg.error())
            break

    # Process the received message
    print('Received message: {}'.format(msg.value().decode('utf-8')))