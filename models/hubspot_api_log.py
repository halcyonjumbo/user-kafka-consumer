from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, Integer, text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from config.database import DB_CONFIG

Base = declarative_base()

class HubspotApiLog(Base):
    __tablename__ = 'hubspot_api_log'
    __table_args__ = {'schema': DB_CONFIG['schema']}

    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    endpoint = Column(String(256), nullable=False)
    request = Column(String(256))
    response = Column(String(256))
    status = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime)
    deleted = Column(Boolean, nullable=False, default=False)