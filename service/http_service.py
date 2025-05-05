import requests
class HttpService:
    """Class for HTTP service"""
    def __init__(self):
        pass
    
    def call(self, method, endpoint, headers=None, json=None):
            """Make HTTP request with given parameters"""
            try:
                response = requests.request(
                    method=method,
                    url=endpoint,
                    headers=headers,
                    json=json
                )
                return response
            except requests.exceptions.RequestException as e:
                raise Exception(f"HTTP request failed: {str(e)}")

        