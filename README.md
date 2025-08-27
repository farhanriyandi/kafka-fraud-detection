# kafka-fraud-detection
A simple Kafka-based data pipeline for fraud detection.  
It simulates transactions, detects fraud risk, and publishes transformed messages.

## How to run
1. Clone the repo
    ```
    git clone https://github.com/farhanriyandi/kafka-fraud-detection.git
    cd kafka-fraud-detection
    ```   
2. Start the docker containers
    ```
    docker compose up -d
    ```
   You can open Kafka UI (web dashboard) at:  
    👉 [http://localhost:8080/](http://localhost:8080/)

3. Create 2 topics (transactions and transactions_scored):

   * Open a shell inside the Kafka container:
     ```bash
     docker exec -it my-kafka bash
     ```
     
     **Note:** If you are using Linux and encounter permission issues, try:
     ```
     sudo chown -R 1001:1001 ./dockervol/kafka
     docker compose up -d
     ```
     Then repeat the step ```docker exec -it my-kafka bash ``` above.
    
   * Create `transactions` topic:
     ```bash
     kafka-topics.sh --create --topic transactions --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
     ```

   * Create `transactions_scored` topic:
     ```bash
     kafka-topics.sh --create --topic transactions_scored --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
     ```

   * List topics:
     ```bash
     kafka-topics.sh --bootstrap-server localhost:9092 --list
     ```

   * Describe topics:
     ```bash
     kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic transactions
     kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic transactions_scored
     ```

4. Create a virtual environment **for Linux/macOS:**
   ```
    python3 -m venv .venv
   ```
   ```
   source .venv/bin/activate
   ```
   **Note:** You can use other methods to create and activate a virtual environment depending on your operating system or personal preference.

5. Install the dependencies
    ```
    pip install -r requirements.txt
    ```
    
6. Run the Python Scripts
   * Terminal 1 → Run the consumer + transformer (so it’s ready to receive data and apply transformations immediately):
     ```
     python3 fraud_detection_pipeline/consumer_transformer.py
     ```
   * Terminal 2 → Run the data generator + producer (to send data into Kafka):
     ```
     python3 fraud_detection_pipeline/data_generator.py
     ```

