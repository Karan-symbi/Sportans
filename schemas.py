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


# ---------- Events ----------

class EventCreate(BaseModel):
    eventType: str
    eventDate: date
    eventTime: time
    location: str
    description: str


class EventResponse(BaseModel):
    id: int
    eventType: str
    eventDate: date
    eventTime: time
    location: str
    description: str


class FitnessRequest(BaseModel):
    age: int
    height: float   # in cm
    weight: float   # in kg
    gender: Literal["Male", "Female", "Other"]


class FitnessResponse(BaseModel):
    bmi: float
    bmr: float
    fitness_recommendations: str
    diet_recommendations: str

class TeamCreate(BaseModel):
    team_name: str
    state: str
    district: str


class PlayerAdd(BaseModel):
    team_name: str
    player_name: str
    role: str
    contact: str
    email: str


class JoinRequest(BaseModel):
    team_name: str
    player_name: str


class PlayerResponse(BaseModel):
    id: int
    name: str
    email: str



class PlayerStatsCreate(BaseModel):
    player_id: int
    goals_scored: int
    assists: int
    other_metrics: Optional[str] = None


class PlayerStatsResponse(BaseModel):
    id: int
    player_id: int
    goals_scored: int
    assists: int
    other_metrics: Optional[str]


class FeedbackCreate(BaseModel):
    name: str
    content: str
