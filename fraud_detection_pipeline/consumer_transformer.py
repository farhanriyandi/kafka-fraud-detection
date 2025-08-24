import json
import time
from kafka import KafkaConsumer, KafkaProducer

BOOTSTRAP_SERVER = "localhost:9092"
TOPIC_NAME = "transactions"

NEW_TOPIC_NAME = "transactions_scored"

# Consumer (raw transactions)
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=BOOTSTRAP_SERVER,
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

# Producer (for transformed data)
producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def fraud_rules(tx):
    risk_score = 0
    # Rule 1: High amount
    if tx["amount"] > 5000:
        risk_score += 50
    # Rule 2: Foreign location
    if tx["location"] == "Tokyo":
        risk_score += 30
    # Rule 3: Unusual device
    if tx["device_id"] == "Web":
        risk_score += 20
    return risk_score

for msg in consumer:
    tx = msg.value
    risk_score = fraud_rules(tx)
    tx["fraud_flag"] = risk_score >= 50   # True if high risk
    tx["risk_score"] = risk_score
    tx["processed_at"] = time.time()

    # Send to new topic
    producer.send(NEW_TOPIC_NAME, tx)
    print("Transformed & Sent:", tx)
