from pydantic import BaseModel, EmailStr

class CompanyDTO(BaseModel):
    name: str
    legal_name: str
    nit: str
    country: str
    location: str
    phone: int
    email: EmailStr
    postal_code: str
    website: str
    contact_name: str
    contact_phone: str
    contact_email: EmailStr
    notes: str
    status: bool

    class Config:
        orm_mode = True