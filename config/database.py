from typing import Dict, Any
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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