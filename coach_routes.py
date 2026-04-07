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


@router.post("/add-player")
def add_player(data: PlayerAdd):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM players WHERE name=%s", (data.player_name,))
    player = cursor.fetchone()

    if not player:
        raise HTTPException(status_code=404, detail="Player not registered")

    cursor.execute("SELECT id FROM teams WHERE team_name=%s", (data.team_name,))
    team = cursor.fetchone()

    if not team:
        raise HTTPException(status_code=404, detail="Team not found")

    cursor.execute(
        "INSERT INTO t_players (name, role, contact_phone, contact_email) VALUES (%s,%s,%s,%s)",
        (data.player_name, data.role, data.contact, data.email)
    )
    conn.commit()

    cursor.execute(
        "INSERT INTO team_player (team_id, player_id) VALUES (%s,%s)",
        (team[0], player[0])
    )
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Player added to team successfully"}
