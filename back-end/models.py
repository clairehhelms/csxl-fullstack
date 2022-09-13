from pydantic import BaseModel

class LinkCreate(BaseModel):
    display_name: str
    url: str