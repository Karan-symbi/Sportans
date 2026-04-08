from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time
from typing import Literal


# ---------- Sporta Bot (Chat) ----------

class ChatMessage(BaseModel):
    role: Literal["system", "human", "ai"]
    content: str


class ChatRequest(BaseModel):
    username: str
    message: str
    history: List[ChatMessage] = []


class ChatResponse(BaseModel):
    reply: str
    history: List[ChatMessage]


# ---------- Sporta Coach (Form-based) ----------

class CoachRequest(BaseModel):
    username: str
    sport: str
    skill: str
    level: str
    trainingFrequency: int
    goal: str
    challenges: str
    specificRequest: Optional[str] = None

class CoachResponse(BaseModel):
    plan: str


