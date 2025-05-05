from pydantic import BaseModel, Field
from typing import Optional

class Properties(BaseModel):
    """Class for User Properties"""
    country_code: Optional[str] = None
    email: Optional[str] = None
    mobilephone: Optional[str] = None
    lastname: Optional[str] = None
    firstname: Optional[str] = None
    docquity_database_id: Optional[int] = None
    usercode: Optional[str] = None
    specialty: Optional[str] = None
    city: Optional[str] = None

class CreateContactDto(BaseModel):
    """Class for Create Contact DTO"""
    properties: Properties