import database
print("Using database.py from:", database.__file__)

from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Flashcard
from schemas import FlashcardCreate, FlashcardOut
from subject_classifier import classify_subject
import random

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/flashcard")
def add_flashcard(flashcard: FlashcardCreate, db: Session = Depends(get_db)):
    subject = classify_subject(flashcard.question)
    new_card = Flashcard(
        student_id=flashcard.student_id,
        question=flashcard.question,
        answer=flashcard.answer,
        subject=subject
    )
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return {"message": "Flashcard added successfully", "subject": subject}


@app.get("/get-subject", response_model=list[FlashcardOut])
def get_flashcards(student_id: str = Query(...), limit: int = Query(5), db: Session = Depends(get_db)):
    all_cards = db.query(Flashcard).filter(Flashcard.student_id == student_id).all()

    subject_map = {}
    for card in all_cards:
        subject_map.setdefault(card.subject, []).append(card)

    mixed = []
    subjects = list(subject_map.keys())
    random.shuffle(subjects)

    for subject in subjects:
        if subject_map[subject]:
            mixed.append(subject_map[subject].pop(0))
        if len(mixed) >= limit:
            break

    return mixed

@app.get("/")
def root():
    return {"message": "Welcome to the Flashcards API!"}

