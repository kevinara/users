from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[str]
    name: str
    user_name: str
    user_passwd: str
