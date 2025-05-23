from datetime import datetime
from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from config.database import DB_CONFIG
Base = declarative_base()

class ContactsMaster(Base):
    """SQLAlchemy model for contacts_master table"""
    __tablename__ = 'contacts_master'
    __table_args__ = {'schema': DB_CONFIG['schema']}

    id = Column(BigInteger, primary_key=True, nullable=False)
    hubspot_id = Column(String(255))
    veeva_id = Column(String(255))
    number_of_deals_associated = Column(String(255))
    number_of_products_associated = Column(String(255))
    hs_marketable_status = Column(String(255))
    lastmodifieddate = Column(DateTime)
    hs_is_unworked = Column(String(255))
    dq_customer_source_id__c_ = Column(String(255))
    num_associated_deals = Column(String(255))
    docquity_last_activity_date = Column(DateTime)
    notes_next_activity_date = Column(DateTime)
    do_not_call_new_value = Column(String(255))
    delete = Column(String(255))
    notes_comments_for_reference = Column(String(255))
    comments_or_notes_for_reference = Column(String(255))
    hs_object_id = Column(String(255))
    hs_object_source_label = Column(String(255))
    createdate = Column(DateTime)
    lifecyclestage = Column(String(255))
    firstname = Column(String(255))
    dq_persona = Column(String(255))
    theme_preference = Column(String(255))
    docquity_database_id = Column(String(255))
    hs_email_domain = Column(String(255))
    hs_updated_by_user_id = Column(String(255))
    lastname = Column(String(255))
    country_code = Column(String(255))
    specialty = Column(String(255))
    hs_created_by_user_id = Column(String(255))
    dq_permission_access = Column(String(255))
    no_email = Column(String(255))
    no_video_call = Column(String(255))
    no_chat_or_text = Column(String(255))
    do_not_call = Column(String(255))
    record_type = Column(String(255))
    no_face_to_face = Column(String(255))
    no_phone_call = Column(String(255))
    associations = Column(String(256))
    multiple_specialty = Column(String(256))
    first_deal_created_date = Column(DateTime)
    hs_time_between_contact_creation_and_deal_creation = Column(String(255))
    dq_channels_followed = Column(String(65535))
    owner_1 = Column(String(255))
    hubspot_owner_id = Column(String(255))
    hubspot_team_id = Column(String(255))
    company = Column(String(255))
    owner_2 = Column(String(255))
    business_type = Column(String(255))
    remove_novartis_product = Column(String(255))
    middle_name = Column(String(255))
    owner_3 = Column(String(255))
    owner_4 = Column(String(255))
    owner_5 = Column(String(255))
    age = Column(String(255))
    address = Column(String(256))
    owner_6 = Column(String(255))
    city = Column(String(255))
    hco_primary_address__primary_city_ = Column(String(255))
    temporary_contact = Column(String(255))
    owner_7 = Column(String(255))
    dq_client_level_territory__c = Column(String(255))
    no_visit = Column(String(255))
    hs_email_hard_bounce_reason_enum = Column(String(255))
    ta_channel_subscription = Column(String(255))
    street_address_2 = Column(String(255))
    owner_8 = Column(String(255))
    hcp_status = Column(String(255))
    zip = Column(String(255))
    hcp_specialty = Column(String(255))
    owner_9 = Column(String(255))
    date_of_birth = Column(Date)
    jobtitle = Column(String(255))
    maiden_name = Column(String(255))
    hcp_type = Column(String(255))
    hs_merged_object_ids = Column(String(255))
    practice_type__govt___private_ = Column(String(255))
    state = Column(String(255))
    sub_specialty = Column(String(255))
    client_territory = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)
    docquity_database_id = Column(String)
    usercode = Column(String(50))