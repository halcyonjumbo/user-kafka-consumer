from typing import Dict, Any
import os

# Kafka configuration settings
KAFKA_CONFIG: Dict[str, Any] = {
    'bootstrap_servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092'),
    'group_id': os.getenv('KAFKA_GROUP_ID', 'hubspot_consumer_group'),
    'auto_offset_reset': os.getenv('KAFKA_AUTO_OFFSET_RESET', 'earliest'),
    'enable_auto_commit': os.getenv('KAFKA_ENABLE_AUTO_COMMIT', 'true').lower() == 'true',
    'auto_commit_interval_ms': int(os.getenv('KAFKA_AUTO_COMMIT_INTERVAL_MS', '5000')),
    'session_timeout_ms': int(os.getenv('KAFKA_SESSION_TIMEOUT_MS', '60000')),
    'heartbeat_interval_ms': int(os.getenv('KAFKA_HEARTBEAT_INTERVAL_MS', '20000')),
}

# Topic configuration
TOPIC_CONFIG: Dict[str, str] = {
    'create_user': os.getenv('KAFKA_CREATE_USER_TOPIC', 'kafka_docquity_tcp_gateway_usercreation'),
}

# Consumer configuration
CONSUMER_CONFIG: Dict[str, Any] = {
    'max_poll_records': int(os.getenv('KAFKA_MAX_POLL_RECORDS', '100')),
    'max_poll_interval_ms': int(os.getenv('KAFKA_MAX_POLL_INTERVAL_MS', '300000')),
    'fetch_max_bytes': int(os.getenv('KAFKA_FETCH_MAX_BYTES', '52428800')),
    'fetch_min_bytes': int(os.getenv('KAFKA_FETCH_MIN_BYTES', '1')),
    'fetch_max_wait_ms': int(os.getenv('KAFKA_FETCH_MAX_WAIT_MS', '500')),
} 