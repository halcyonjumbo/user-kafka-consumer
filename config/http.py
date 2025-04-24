from typing import Dict, Any
import os

# HubSpot API configuration
HUBSPOT_CONFIG: Dict[str, Any] = {
    'base_url': os.getenv('HUBSPOT_BASE_URL', 'https://api.hubapi.com'),
    'api_key': os.getenv('HUBSPOT_API_KEY', ''),
}