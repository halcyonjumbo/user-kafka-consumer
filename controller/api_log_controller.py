from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dto.request.hubspot_api_log_dto import HubspotApiLogDto
from dto.response.base_reponse import BaseResponse
from repository.hubspot_api_log_repo import HubspotApiLogRepository
from repository.redshift_connection import RedshiftConnection
from service.hubspot_api_log_service import HubspotApiLogService



service = HubspotApiLogService(HubspotApiLogRepository(RedshiftConnection()))

router = APIRouter(prefix="/api-logs", tags=["Api Logs"])

@router.post("/", response_model=BaseResponse)
def create_api_log(hubspot_api_log: HubspotApiLogDto):
    return service.create_new_api_log(hubspot_api_log)