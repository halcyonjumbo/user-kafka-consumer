from pydantic import BaseModel

class HubspotApiLogResponseDto(BaseModel):
    id: int
    endpoint: str
    request: str
    response: str