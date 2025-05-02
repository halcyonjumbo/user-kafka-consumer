from pydantic import BaseModel

class HubspotApiLogDto(BaseModel):
    endpoint: str
    request: str
    response: str
    status: int