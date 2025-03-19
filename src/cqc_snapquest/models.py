from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from cqc_snapquest.database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String(20), unique=True, nullable=False)
    registered_at = Column(DateTime, default=datetime.utcnow)


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    creator_phone = Column(String(20), ForeignKey("users.phone_number"), nullable=False)
    game_code = Column(String(10), unique=True, nullable=False)

    locations = relationship("Location", back_populates="game")


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"), nullable=False)
    description = Column(String(255), nullable=False)
    expected_image_url = Column(String(255), nullable=False)
    solved_by_user = Column(String(20), ForeignKey("users.phone_number"), nullable=True)

    game = relationship("Game", back_populates="locations")


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    user_phone = Column(String(20), ForeignKey("users.phone_number"), nullable=False)
    game_code = Column(String(10), ForeignKey("games.game_code"), nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    submitted_image_url = Column(String(255), nullable=False)
    is_correct = Column(Boolean, default=False)
    submitted_at = Column(DateTime, default=datetime.utcnow)
