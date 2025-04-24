import json
import logging
import signal
import sys
from kafka import KafkaConsumer
from config.kafka import KAFKA_CONFIG, TOPIC_CONFIG
from repository.redshift_connection import RedshiftConnection
from dto.request.create_user_kafka_dto import CreateUserKafkaDto, UserDetails
from service.hubspot_service import HubspotService
from repository.user_master_mapping_repo import UserMasterMappingRepository
from util.logger_util import LoggerUtil
from service.http_service import HttpService

logger = LoggerUtil().get_logger(__name__)

def signal_handler(signum, frame):
    logger.info(f"Received signal {signum}. Shutting down...")
    sys.exit(0)

def process_kafka_messages():
    """Main function to process Kafka messages"""
    # Create Kafka consumer
    consumer = KafkaConsumer(
        TOPIC_CONFIG['create_user'],
        **KAFKA_CONFIG
    )

    # Initialize components
    redshift_conn = RedshiftConnection()
    http_service = HttpService()
    user_master_mapping_repo = UserMasterMappingRepository(redshift_conn)
    hubspot_service = HubspotService(http_service, user_master_mapping_repo)

    # Set up signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    logger.info("Starting Kafka consumer. Press CTRL+C to exit.")

    try:
        while True:
            try:
                messages = consumer.poll(timeout_ms=1000)
                for topic_partition, records in messages.items():
                    for record in records:
                        # Parse Kafka message
                        event_data = json.loads(json.loads(record.value.decode('utf-8')))
                        
                        # Handle both message formats
                        if "userDetails" in event_data:
                            # First format - nested userDetails
                            create_user_dto = CreateUserKafkaDto(**event_data)
                        else:
                            # Second format - flat structure
                            create_user_dto = CreateUserKafkaDto(
                                user_details=UserDetails(**event_data),
                                created_by=event_data.get("createdBy"),
                                module=event_data.get("module")
                            )

                        # Consumser Handler
                        hubspot_service.create_user_kafka(create_user_dto)
                        
                        
                        
            except Exception as e:
                logger.error(f"Error processing message: {str(e)}")
                continue

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
    finally:
        logger.info("Shutting down consumer...")
        consumer.close()
        RedshiftConnection.close_connection()

if __name__ == "__main__":
    process_kafka_messages()