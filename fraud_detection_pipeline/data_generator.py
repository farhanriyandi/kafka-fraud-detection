import json
import random
import time
import uuid
from kafka import KafkaProducer

BOOTSTRAP_SERVER = "localhost:9092"
TOPIC_NAME = "transactions"
# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers= BOOTSTRAP_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

users = ["U001", "U002", "U003", "U004"]
locations = ["Jakarta", "Bandung", "Surabaya", "Tokyo"]
devices = ["iOS", "Android", "Web"]

def generate_transaction():
    return {
        "transaction_id": str(uuid.uuid4()),
        "user_id": random.choice(users),
        "amount": random.randint(10, 10000),
        "location": random.choice(locations),
        "device_id": random.choice(devices),
        "timestamp": time.time()
    }

if __name__ == "__main__":
    while True:
        tx = generate_transaction()
        producer.send(TOPIC_NAME, tx)
        print("Produced:", tx)
        time.sleep(1)
