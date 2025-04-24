from models.hubspot_api_log import HubspotApiLog
from sqlalchemy.orm import Session

class HubspotApiLogRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, hubspot_api_log: HubspotApiLog):
        self.session.add(hubspot_api_log)
        self.session.commit()   