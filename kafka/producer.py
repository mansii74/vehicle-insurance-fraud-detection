import json
import time
import pandas as pd
from kafka import KafkaProducer

# Kafka configuration
KAFKA_TOPIC = "insurance_claims"
KAFKA_BROKER = "localhost:9092"

def create_producer():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    return producer

def stream_csv_to_kafka(csv_file):
    producer = create_producer()
    df = pd.read_csv(csv_file)

    print("Starting Kafka producer...")

    for index, row in df.iterrows():
        record = row.to_dict()
        producer.send(KAFKA_TOPIC, value=record)
        print(f"Sent record {index + 1}")
        time.sleep(1)   # simulate real-time streaming

    producer.flush()
    producer.close()
    print("Data streaming completed.")

if __name__ == "__main__":
    stream_csv_to_kafka("Dataset/Processed_clean_carclaims.csv")
