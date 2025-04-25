from pydantic import BaseModel, Field
from typing import Optional

class UserDetails(BaseModel):
    """Class for User Details"""
    email: Optional[str] = None
    firstName: Optional[str] = None
    middleName: Optional[str] = None
    lastName: Optional[str] = None
    gender: Optional[str] = None
    countryCode: Optional[str] = None
    phoneno: Optional[str] = None
    userType: Optional[str] = None
    profilePic: Optional[str] = None
    profilePicBucket: Optional[str] = None
    profilePicFileType: Optional[str] = None
    verificationStatus: Optional[str] = None
    user_status: Optional[str] = None
    uuid: Optional[str] = None
    userCode: Optional[str] = None
    module: Optional[str] = None
    createdBy: Optional[str] = None
    customId: Optional[str] = None
    
class CreateUserKafkaDto(BaseModel):
    """Class for Create User Kafka DTO"""
    createdBy: Optional[str] = None
    module: Optional[str] = None
    userDetails: Optional[UserDetails] = None
    platformId: Optional[str] = None
    platformName: Optional[str] = None
    isJourneyCompleted: Optional[bool] = False
    subModule: Optional[str] = None
    isPurple: Optional[bool] = False
