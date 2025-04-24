from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from config.database import DB_CONFIG
Base = declarative_base()

class UserMasterMapping(Base):
    """SQLAlchemy model for users_master_mapping table"""
    __tablename__ = 'users_master_mapping'
    __table_args__ = {'schema': DB_CONFIG['schema']}

    id = Column(Integer, primary_key=True)
    hubspot_id = Column(String)
    docquity_database_id = Column(String)
    usercode = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False) 