import pydantic
import nanoid
from datetime import datetime

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
        m = str(values["BirthMonth"]).zfill(2)
        d = str(values["BirthDay"]).zfill(2)
        return v or f"{m}:{d}"

    @pydantic.validator("CreatedAt", pre=True, always=True)
    def default_created(cls, v):
        return v or datetime.now().isoformat()
    
    # @pydantic.field_serializer("CreatedAt")
    # def serialize_created(self, ts, _):
    #     return datetime.now().isoformat()
    
    @pydantic.validator("UpdatedAt", pre=True, always=True)
    def default_modified(cls, v, *, values):
        return v or values["CreatedAt"]

    # @pydantic.field_serializer("UpdatedAt")
    # def serialize_created(self, ts, _):
    #     return datetime.now().isoformat()
    
    