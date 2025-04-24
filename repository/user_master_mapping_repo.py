from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from repository.redshift_connection import RedshiftConnection
from models.user_master_mapping import UserMasterMapping

class UserMasterMappingRepository:
    """Repository for User Master Mapping in Redshift using SQLAlchemy"""
    
    def __init__(self, redshift_connector: RedshiftConnection):
        self.session = redshift_connector.get_session()

    def create(self, hubspot_id, docquity_database_id, usercode):
        """Create Users Master Mapping"""
        try:
            user_mapping = UserMasterMapping(
                hubspot_id=hubspot_id,
                docquity_database_id=docquity_database_id,
                usercode=usercode,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            
            self.session.add(user_mapping)
            self.session.commit()
            
        except SQLAlchemyError as e:
            self.session.rollback()
            raise Exception(f"Failed to store user master mapping in Redshift: {str(e)}")
         
        
    def find_by_docquity_database_usercode_or_id(self, usercode, docquity_database_id) -> UserMasterMapping:
        """Find Users Master Mapping by docquity_database_id or usercode"""
        try:
            if usercode is not None:
                result = self.session.query(UserMasterMapping).filter(
                    UserMasterMapping.usercode == usercode,
                    UserMasterMapping.deleted == False
                ).first()
            elif docquity_database_id is not None and docquity_database_id != 0:
                result = self.session.query(UserMasterMapping).filter(
                    UserMasterMapping.docquity_database_id == docquity_database_id,
                    UserMasterMapping.deleted == False
                ).first()
            else:
                raise Exception("Either usercode or docquity_database_id must be provided")
            
            return result

        except SQLAlchemyError as e:
            raise Exception(f"Failed to find user master mapping: {str(e)}")
    
