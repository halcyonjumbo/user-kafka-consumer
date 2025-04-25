from models.hubspot_api_log import HubspotApiLog
from repository.redshift_connection import RedshiftConnection

class HubspotApiLogRepository:
    def __init__(self, redshift_connector: RedshiftConnection):
        self.session = redshift_connector.get_session()

    def create(self, hubspot_api_log: HubspotApiLog):
        self.session.add(hubspot_api_log)
        self.session.commit()   