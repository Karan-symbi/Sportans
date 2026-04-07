from fastapi import APIRouter, HTTPException
from database import get_db_connection
from schemas import TeamCreate, PlayerAdd

router = APIRouter(prefix="/coach", tags=["Coach"])


@router.post("/team")
def create_team(data: TeamCreate):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO teams (team_name, state, district) VALUES (%s, %s, %s)",
        (data.team_name, data.state, data.district)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Team created successfully"}


@router.get("/teams")
def list_teams():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM teams")
    teams = cursor.fetchall()

    cursor.close()
    conn.close()

    return teams


