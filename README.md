# kafka-fraud-detection

## How to run
1. Clone the repo
    ```
    git clone 
    ```   
2. Start the docker containers
    ```
    docker compose up -d
    ```     

3. Create 2 topics (transactions and transactions_scored):
   create transactions topic:
   ```
   kafka-topics.sh --create --topic transactions --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
   ```

   create transactions_scored topic:
   ```
   kafka-topics.sh --create --topic transactions_scored --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
   ```

4. Create a virtual environment **For Linux/macOS:**
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
     python consumer_transformer.py
     ```
   * Terminal 2 → Run the data generator + producer (to send data into Kafka):
     ```
     python data_generator.py
     ```
