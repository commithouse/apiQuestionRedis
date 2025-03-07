from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis

app = FastAPI()

class Question(BaseModel):
    question_text: str
    question_id: int

IP_CONTAINER = "20.206.150.156"

def get_redis_connection():
    try:
        return redis.Redis(host=IP_CONTAINER, port=6379, decode_responses=True)
    except redis.RedisError as e:
        raise HTTPException(status_code=500, detail="Could not connect to Redis")

@app.get("/question/{question_key}")
def get_question(question_key: str):
    r = get_redis_connection()
    question = r.hgetall("question:" + question_key)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@app.post("/question")
def create_question(question: Question):
    r = get_redis_connection()
    
    if r.hget("question:" + str(question.question_id), "question_text") is not None:
        raise HTTPException(status_code=400, detail="Question already exists")

    r.hset(f'question:{question.question_id}', 'question_text', question.question_text)
    return {"message": "Question has been created"}


@app.delete("/question/{question_key}")
def delete_question(question_key: str):
    r = get_redis_connection()
    if r.hgetall("question:" + question_key) == {}:
        raise HTTPException(status_code=404, detail="Question not found")
    r.delete("question:" + question_key)
    return {"message": "Question has been deleted"}


@app.put("/question/{question_key}")
def update_question(question_key: str, question: Question):
    r = get_redis_connection()
    if r.hgetall("question:" + question_key) == {}:
        raise HTTPException(status_code=404, detail="Question not found")
    r.hset("question:" + question_key, "question_text", question.question_text)
    return {"message": "Question has been updated"}
