from datetime import datetime
from models.hubspot_api_log import HubspotApiLog
from repository.redshift_connection import RedshiftConnection
from util.logger_util import LoggerUtil

class HubspotApiLogRepository:
    def __init__(self, redshift_connector: RedshiftConnection):
        self.session = redshift_connector.get_session()
        self.conn = redshift_connector.get_connection()
        self.logger = LoggerUtil().get_logger(self.__class__.__name__)

    def insert(self, endpoint, request, response, status):
        # Define your data
        created_at = datetime.now()
        updated_at = datetime.now()
        deleted = False

        # INSERT statement (do NOT include ID — Redshift will handle it)
        insert_query = """
        INSERT INTO hubspot_etl_sandbox.hubspot_api_log (
            endpoint, request, response, status, created_at, updated_at, deleted
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Execute the insert
        with self.conn.cursor() as cursor:
            cursor.execute(insert_query, (
                endpoint, request, response, status, created_at, updated_at, deleted
            ))
            self.conn.commit()

    def find_latest_api_log(self) -> HubspotApiLog:
        return self.session.query(HubspotApiLog).filter(
                    HubspotApiLog.deleted == False
                ).order_by(HubspotApiLog.created_at.desc()).limit(1).first()
