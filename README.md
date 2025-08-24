# kafka-fraud-detection

## How to run
1. Clone the repo
    ```
    git clone https://github.com/farhanriyandi/kafka-fraud-detection.git
    ```   
2. Start the docker containers
    ```
    docker compose up -d
    ```     

3. Create 2 topics (transactions and transactions_scored):

   * **Open a shell inside container:**
   ```
   docker exec -it my-kafka bash
   ```
   
   * **Create transactions topic:**
   ```
   kafka-topics.sh --create --topic transactions --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
   ```

   * **Create transactions_scored topic:**
   ```
   kafka-topics.sh --create --topic transactions_scored --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
   ```

   * **List topics:**
   ```
   kafka-topics.sh --bootstrap-server localhost:19092 --list
   ```

   * **Describe topics:**
    ```
    kafka-topics.sh --bootstrap-server localhost:19092 --describe --topic transactions
    ```

    ```
    kafka-topics.sh --bootstrap-server localhost:19092 --describe --topic transactions_scored
    ```

5. Create a virtual environment **For Linux/macOS:**
   ```
    python3 -m venv .venv
   ```
   ```
   source .venv/bin/activate
   ```
   **Note:** You can use other methods to create and activate a virtual environment depending on your operating system or personal preference.

6. Install the dependencies
    ```
    pip install -r requirements.txt
    ```
7. Run the Python Scripts
   * Terminal 1 → Run the consumer + transformer (so it’s ready to receive data and apply transformations immediately):
     ```
     python3 consumer_transformer.py
     ```
   * Terminal 2 → Run the data generator + producer (to send data into Kafka):
     ```
     python3 data_generator.py
     ```
