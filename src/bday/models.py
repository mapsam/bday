import pydantic
import nanoid
from datetime import datetime
from bday.util import build_dt

class Bday(pydantic.BaseModel):
    Id: str = None
    Name: str
    BirthMonth: int
    BirthDay: int
    BirthDt: str = None
    BirthYear: int = None
    CreatedAt: str = None
    UpdatedAt: str = None

    @pydantic.validator("Id", pre=True, always=True)
    def default_id(cls, v):
        return nanoid.generate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 10)
    
    @pydantic.validator("BirthDt", pre=True, always=True)
    def default_dt(cls, v, *, values):
        dt = build_dt(day=values["BirthDay"], month=values["BirthMonth"])
        return v or dt

    @pydantic.validator("CreatedAt", pre=True, always=True)
    def default_created(cls, v):
        return v or datetime.now().isoformat()
        
    @pydantic.validator("UpdatedAt", pre=True, always=True)
    def default_modified(cls, v, *, values):
        return v or values["CreatedAt"]    
    