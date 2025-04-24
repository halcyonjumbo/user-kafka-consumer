from dto.request.create_contact_dto import CreateContactDto, Properties
from dto.request.create_user_kafka_dto import CreateUserKafkaDto
from repository.user_master_mapping_repo import UserMasterMappingRepository
from service.http_service import HttpService
from config.http import HUBSPOT_CONFIG
from repository.redshift_connection import RedshiftConnection

class HubspotService:
    """Class for Hubspot service"""

    http_service: HttpService
    user_master_mapping_repo: UserMasterMappingRepository

    def __init__(self, http_service: HttpService = None, user_master_mapping_repo: UserMasterMappingRepository = None):
            self.http_service = http_service or HttpService()
            self.user_master_mapping_repo = user_master_mapping_repo or UserMasterMappingRepository(RedshiftConnection())
        
    def prepare_create_contact_dto(self, create_user_kafka_dto: CreateUserKafkaDto):
        """Prepare create contact dto"""
        properties = Properties(
            country_code=create_user_kafka_dto.user_details.country_code,
            email=create_user_kafka_dto.user_details.email,
            mobile_phone=create_user_kafka_dto.user_details.phone_no,
            last_name=create_user_kafka_dto.user_details.last_name,
            first_name=create_user_kafka_dto.user_details.first_name,
            docquity_database_id=0,
            user_code=create_user_kafka_dto.user_details.user_code,
            specialty='',
            city=''
        )
        return CreateContactDto(
            properties=properties
        )
    
    def create_user_in_hubspot(self, create_user_kafka_dto: CreateUserKafkaDto):
        """Create user in Hubspot"""
        try:
            response = self.http_service.call(
                method='POST',
                url=f'{HUBSPOT_CONFIG["base_url"]}/crm/v3/objects/contacts',
                headers= {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': f'Bearer {HUBSPOT_CONFIG["api_key"]}'
                },
                data=self.prepare_create_contact_dto(create_user_kafka_dto).model_dump()
            )
            return response
        except Exception as e:
            raise Exception(f"Failed to create user in Hubspot: {str(e)}")

    def create_user_kafka(self, create_user_kafka_dto: CreateUserKafkaDto):
        """Find user in User Master Mapping table and create user in Hubspot if not exists"""
        try:
            user_master_mapping = self.user_master_mapping_repo.find_by_docquity_database_usercode_or_id(create_user_kafka_dto.user_details.user_code, 0)
            if user_master_mapping is None:
                response = self.create_user_in_hubspot(create_user_kafka_dto)
                if response.status_code == 200:
                    hubspot_id = response.json().get('id')
                    self.user_master_mapping_repo.create(hubspot_id, 0, create_user_kafka_dto.user_details.user_code)
                else:
                    raise Exception("Failed to create user in Hubspot")
            else:
                raise Exception("User already exists in Hubspot")
        except Exception as e:
            raise Exception(f"Failed to create user Kafka: {str(e)}")
