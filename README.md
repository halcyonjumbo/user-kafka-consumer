# HubSpot Kafka Consumer

This is a Kafka consumer that processes events from a Kafka topic, makes HTTP requests to a specified API endpoint, and stores the responses in Amazon Redshift.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Configure the settings in `.env`:
   - Update Kafka configuration (bootstrap servers, topic name)
   - Set your API endpoint and authentication details
   - Configure Redshift connection details

## Usage

Run the consumer:
```bash
python consumer.py
```

The consumer will:
1. Connect to Kafka and start listening to the specified topic
2. For each message received:
   - Parse the message
   - Make an HTTP request to the configured API endpoint
   - Store the API response in Redshift
3. Log all errors


## Error Handling

- The consumer writes all error reponses to a log table and continues processing
- Failed API requests are logged but don't stop the consumer