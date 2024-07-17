from typing import List

from pydantic import BaseModel, EmailStr


class Email(BaseModel):
    sender: EmailStr
    recipients: List[EmailStr]
    subject: str
    body_text: str = ""
    body_html: str = ""
