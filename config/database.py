from typing import Dict, Any
import os

# Database connection configuration
DB_CONFIG: Dict[str, Any] = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', '5432')),
    'database': os.getenv('DB_NAME', 'hubspot_db'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'postgres'),
    'schema': os.getenv('DB_SCHEMA', 'public'),
    'min_connections': int(os.getenv('DB_MIN_CONNECTIONS', '1')),
    'max_connections': int(os.getenv('DB_MAX_CONNECTIONS', '10')),
    'connect_timeout': int(os.getenv('DB_CONNECT_TIMEOUT', '10')),
}

# Table configuration
TABLE_CONFIG: Dict[str, str] = {
    'users_master_mapping': os.getenv('DB_USERS_MASTER_MAPPING_TABLE', 'users_master_mapping'),
}

# Query configuration
QUERY_CONFIG: Dict[str, Any] = {
    'batch_size': int(os.getenv('DB_BATCH_SIZE', '1000')),
    'timeout': int(os.getenv('DB_QUERY_TIMEOUT', '30')),
} 