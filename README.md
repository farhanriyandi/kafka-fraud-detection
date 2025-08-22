# How to Run

- Clone the repo
    ```
    git clone https://github.com/ammfat/apache-kafka-101.git
    ```

- Start the docker containers
    ```
    docker-compose up -d
    docker ps
    ```

    Ensure the containers are running

- Access the Kafka UI at http://localhost:8080


# Kafka CLI Commands

- Open a shell inside the container
    ```
    docker exec -it kafka bash
    ```

- List topics
    ```
    kafka-topics.sh --bootstrap-server localhost:19092 --list
    ```

- Create a topic
    ```
    kafka-topics.sh --bootstrap-server localhost:19092 --create \
    --topic test-topic \
    --partitions 3 \
    --replication-factor 1
    ```

- Describe the topic
    ```
    kafka-topics.sh --bootstrap-server localhost:19092 --describe --topic test-topic
    ```

- Produce messages
    ```
    kafka-console-producer.sh --bootstrap-server localhost:19092 --topic test-topic
    ```

- Consume messages
    ```
    kafka-console-consumer.sh --bootstrap-server localhost:19092 --topic test-topic --from-beginning
    ```

    or with specific group
    ```
    kafka-console-consumer.sh --bootstrap-server localhost:19092 --topic test-topic --group test-group-cli --from-beginning
    ```


# Kafka Python Client (Simple Producer & Consumer)

- Install the dependencies
    ```
    pip install -r requirements.txt
    ```

- Run the producer
    ```
    python examples/main.py producer
    ```

- Run the consumer
    ```
    python examples/main.py consumer test-group-python
    ```
