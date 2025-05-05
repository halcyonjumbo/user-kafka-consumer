import json
import requests
from dto.request.create_contact_dto import CreateContactDto, Properties
from dto.request.create_user_kafka_dto import CreateUserKafkaDto
from models.hubspot_api_log import HubspotApiLog
from repository.contacts_master_repo import ContactsMasterRepository
from repository.hubspot_api_log_repo import HubspotApiLogRepository
from service.http_service import HttpService
from config.http import HUBSPOT_CONFIG
from repository.redshift_connection import RedshiftConnection
from util.logger_util import LoggerUtil

class HubspotService:
    """Class for Hubspot service"""

    http_service: HttpService
    contacts_master_repo: ContactsMasterRepository
    hubspot_api_log_repo: HubspotApiLogRepository
    logger: LoggerUtil

    def __init__(self, http_service: HttpService = None, contacts_master_repo: ContactsMasterRepository = None, hubspot_api_log_repo: HubspotApiLogRepository = None): 
            self.http_service = http_service or HttpService()
            self.contacts_master_repo = contacts_master_repo or ContactsMasterRepository(RedshiftConnection())
            self.hubspot_api_log_repo = hubspot_api_log_repo or HubspotApiLogRepository(RedshiftConnection())
            self.logger = LoggerUtil().get_logger(self.__class__.__name__)

    def prepare_create_contact_dto(self, create_user_kafka_dto: CreateUserKafkaDto) -> CreateContactDto:
        """Prepare create contact dto"""
        properties = Properties(
            country_code=create_user_kafka_dto.userDetails.countryCode,
            email=create_user_kafka_dto.userDetails.email,
            mobilephone=create_user_kafka_dto.userDetails.phoneno,
            lastname=create_user_kafka_dto.userDetails.lastName,
            firstname=create_user_kafka_dto.userDetails.firstName,
            docquity_database_id=0,
            usercode=create_user_kafka_dto.userDetails.userCode,
            specialty='',
            city=''
        )
        return CreateContactDto(
            properties=properties
        )

    
    def create_user_in_hubspot(self, create_user_kafka_dto: CreateUserKafkaDto) -> requests.Response:
        """Create user in Hubspot"""
        try:
            request_body = self.prepare_create_contact_dto(create_user_kafka_dto).model_dump()
            response = self.http_service.call(
                method='POST',
                endpoint=f'{HUBSPOT_CONFIG["base_url"]}/crm/v3/objects/contacts',
                headers= {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': f'Bearer {HUBSPOT_CONFIG["api_key"]}'
                },
                json=request_body
            )
            if response.status_code != 201:
                self.hubspot_api_log_repo.insert(HubspotApiLog(
                    endpoint='create_contact',
                    request=json.dumps(request_body),
                    response=response.json(),
                    status=response.status_code
                ))
            self.logger.info(f"User created in Hubspot: {response.json()}")
            return response
        except Exception as e:
            raise Exception(f"Failed to create user in Hubspot: {str(e)}")

    def create_user_kafka(self, create_user_kafka_dto: CreateUserKafkaDto) -> None:
        """Find user in User Master Mapping table and create user in Hubspot if not exists"""
        try:
            contacts_master = self.contacts_master_repo.find_by_docquity_database_usercode_or_id(create_user_kafka_dto.userDetails.userCode, 0)
            if contacts_master is None:
                self.create_user_in_hubspot(create_user_kafka_dto)
            else:
                self.logger.info(f"User already exists in Hubspot: {contacts_master.usercode}")
        except Exception as e:
            raise Exception(f"Failed to create user Kafka: {str(e)}")
