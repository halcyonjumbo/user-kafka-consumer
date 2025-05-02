from dto.request.hubspot_api_log_dto import HubspotApiLogDto
from dto.response.base_reponse import HubspotApiLogResponseOut
from dto.response.hubspot_api_log_response_dto import HubspotApiLogResponseDto
from models.hubspot_api_log import HubspotApiLog
from repository.hubspot_api_log_repo import HubspotApiLogRepository
from repository.redshift_connection import RedshiftConnection

class HubspotApiLogService:
    def __init__(self, hubspot_api_log_repo: HubspotApiLogRepository):
        self.hubspot_api_log_repo = hubspot_api_log_repo or HubspotApiLogRepository(RedshiftConnection())

    def create_new_api_log(self, hubspot_api_log: HubspotApiLogDto):
        self.hubspot_api_log_repo.add(hubspot_api_log.endpoint, hubspot_api_log.request, hubspot_api_log.response, hubspot_api_log.status)
        hubspot_api_log_found = self.hubspot_api_log_repo.find_latest_api_log()
        hubspot_api_log_response_dto = self._prepare_hubspot_api_log_response_dto(hubspot_api_log_found)
        if hubspot_api_log_found is not None:
            return HubspotApiLogResponseOut(status="success", message="Hubspot API Log created successfully", data=hubspot_api_log_response_dto)
        else:
            return HubspotApiLogResponseOut(status="error", message="Hubspot API Log creation failed", data=None)

    def _prepare_hubspot_api_log_response_dto(self, hubspot_api_log: HubspotApiLog) -> HubspotApiLogResponseDto:
        return HubspotApiLogResponseDto(
            id=hubspot_api_log.id,
            endpoint=hubspot_api_log.endpoint,
            request=hubspot_api_log.request,
            response=hubspot_api_log.response,
            status=hubspot_api_log.status
        )
        
