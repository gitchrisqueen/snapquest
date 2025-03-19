import random
import string

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from cqc_snapquest.database import SessionLocal, engine
from cqc_snapquest.models import User, Game, Location, Submission, Base
from cqc_snapquest.twilio_handler import send_sms

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register/")
def register_user(phone_number: str, db: Session = Depends(get_db)):
    # Make sure to has +1 and is proper 10 digit number
    if not phone_number.startswith('+1') or len(phone_number) != 12:
        return {"message": "Invalid phone number format. Must be +1 followed by 10 digits."}

    user = db.query(User).filter(User.phone_number == phone_number).first()
    if user:
        return {"message": "User already registered."}

    new_user = User(phone_number=phone_number)
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully."}


@app.post("/create_game/")
def create_game(creator_phone: str, db: Session = Depends(get_db)):
    game_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    game = Game(creator_phone=creator_phone, game_code=game_code)
    db.add(game)
    db.commit()

    send_sms(creator_phone, f"Your game code is: {game_code}")
    return {"message": "Game created!", "game_code": game_code}


@app.post("/add_location/")
def add_location(game_code: str, description: str, expected_image_url: str, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.game_code == game_code).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found.")

    location = Location(game_id=game.id, description=description, expected_image_url=expected_image_url)
    db.add(location)
    db.commit()
    return {"message": "Location added successfully."}


import openai

OPENAI_API_KEY = "your_openai_api_key"
openai.api_key = OPENAI_API_KEY


def generate_riddle(location_description):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Create a riddle for a place described as {location_description}"}]
    )
    return response['choices'][0]['message']['content']


@app.post("/start_game/")
def start_game(phone_number: str, game_code: str, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.game_code == game_code).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found.")

    location = db.query(Location).filter(Location.game_id == game.id, Location.solved_by_user == None).first()
    if not location:
        send_sms(phone_number, "All locations have been solved! Game over.")
        return {"message": "Game over!"}

    riddle = generate_riddle(location.description)
    send_sms(phone_number, f"Find this location: {riddle}")

    return {"riddle": riddle}


@app.post("/submit_image/")
def submit_image(phone_number: str, game_code: str, location_id: int, submitted_image_url: str,
                 db: Session = Depends(get_db)):
    location = db.query(Location).filter(Location.id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found.")

    # Simulate image recognition check
    is_correct = True if "expected" in submitted_image_url else False

    submission = Submission(
        user_phone=phone_number,
        game_code=game_code,
        location_id=location.id,
        submitted_image_url=submitted_image_url,
        is_correct=is_correct
    )

    if is_correct:
        location.solved_by_user = phone_number
        db.commit()
        send_sms(phone_number, "Correct! Move to the next location.")
    else:
        send_sms(phone_number, "Incorrect! Try again.")

    db.add(submission)
    db.commit()
    return {"message": "Submission processed."}
