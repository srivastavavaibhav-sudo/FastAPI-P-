from pydantic import BaseModel


# Schema to create a new user
class CreateUser(BaseModel):
    first_name : str
    last_name : str
    address : str
    address2: str
    district : str
    postal_code : int
    phone : str
    city : str
    Latitude : float
    Longitude : float
    
    class Config:
        orm_mode = True
