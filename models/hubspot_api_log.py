from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class HubspotApiLog(Base):
    __tablename__ = 'hubspot_api_log'

    id = Column(Integer, primary_key=True)
    endpoint = Column(String)
    request_body = Column(String)
    response = Column(String)
    status_code = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime, nullable=True)
    deleted = Column(Boolean, default=False)