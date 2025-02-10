from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Question, Attempt

app = FastAPI()

@app.get("/questions/")
def get_questions(db: Session = Depends(get_db)):
    return db.query(Question).all()

@app.post("/attempts/")
def submit_attempt(user_id: int, question_id: int, user_answer: float, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        return {"error": "Question not found"}
    
    correct = user_answer == question.answer
    attempt = Attempt(user_id=user_id, question_id=question_id, user_answer=user_answer, correct=correct)
    db.add(attempt)
    db.commit()

    if not correct:
        return {"message": "Incorrect answer. AI will generate a new question soon."}
    return {"message": "Correct answer!"}