from kafka import KafkaConsumer

import json


consumer = KafkaConsumer(
    "dummy-topic",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest"
)

print("Worker rodando...")

for event in consumer:
    event = event.value

    print("Evento recebido:", event)

    if event["event"] == "pedido_criado":
        print(f"Processando pedido de {event['payload']['nome']}")