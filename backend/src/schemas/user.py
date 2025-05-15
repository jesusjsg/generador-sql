from datetime import date
from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    created_at: date
    modified_at: date
