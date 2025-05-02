from pydantic import BaseModel
from typing import Any

from dto.response.hubspot_api_log_response_dto import HubspotApiLogResponseDto

class BaseResponse(BaseModel):
    status: str
    message: str
    data: Any

class HubspotApiLogResponseOut(BaseResponse):
    data: HubspotApiLogResponseDto

