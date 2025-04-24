from pydantic import BaseModel, Field
from typing import Optional

class Properties(BaseModel):
    """Class for User Properties"""
    country_code: Optional[str] = None
    email: Optional[str] = None
    mobile_phone: Optional[str] = Field(None, alias="mobilephone")
    last_name: Optional[str] = Field(None, alias="lastname")
    first_name: Optional[str] = Field(None, alias="firstname")
    docquity_database_id: Optional[int] = Field(None, alias="docquity_database_id")
    user_code: Optional[str] = Field(None, alias="usercode")
    specialty: Optional[str] = None
    city: Optional[str] = None

class CreateContactDto(BaseModel):
    """Class for Create Contact DTO"""
    properties: Properties