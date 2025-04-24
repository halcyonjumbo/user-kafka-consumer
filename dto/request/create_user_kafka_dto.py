from pydantic import BaseModel, Field
from typing import Optional

class UserDetails(BaseModel):
    """Class for User Details"""
    email: Optional[str] = None
    first_name: Optional[str] = Field(None, alias="firstName")
    middle_name: Optional[str] = Field(None, alias="middleName")
    last_name: Optional[str] = Field(None, alias="lastName")
    gender: Optional[str] = None
    country_code: Optional[str] = Field(None, alias="countryCode")
    phone_no: Optional[str] = Field(None, alias="phoneno")
    user_type: Optional[str] = Field(None, alias="userType")
    profile_pic_bucket: Optional[str] = Field(None, alias="profilePicBucket")
    profile_pic_file_type: Optional[str] = Field(None, alias="profilePicFileType")
    verification_status: Optional[str] = Field(None, alias="verificationStatus")
    user_status: Optional[str] = Field(None, alias="userStatus")
    uuid: Optional[str] = None
    user_code: Optional[str] = Field(None, alias="userCode")
    module: Optional[str] = None
    created_by: Optional[str] = Field(None, alias="createdBy")
    custom_id: Optional[str] = Field(None, alias="customId")
    
class CreateUserKafkaDto(BaseModel):
    """Class for Create User Kafka DTO"""
    created_by: Optional[str] = Field(None, alias="createdBy")
    module: Optional[str] = Field(None, alias="module")
    user_details: Optional[UserDetails] = Field(None, alias="userDetails")
    platform_id: Optional[str] = Field(None, alias="platformId")
    platform_name: Optional[str] = Field(None, alias="platformName")
    is_journey_completed: Optional[bool] = Field(False, alias="isJourneyCompleted")
    sub_module: Optional[str] = Field(None, alias="subModule")
    is_purple: Optional[bool] = Field(False, alias="isPurple")

class Config:
    allow_population_by_field_name = True