
from pydantic import BaseModel
from typing import List

class UserInput(BaseModel):
    message: str

class BotResponse(BaseModel):
    reply: str
    tasks: List[str]
