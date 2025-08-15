from fastapi import FastAPI
from pydantic import BaseModel
from agent.langchain_agent import answer_question


app = FastAPI()

class QARequest(BaseModel):
    question: str

@app.post('/qa')
async def qa(req: QARequest):
    answer = await answer_question(req.question)
    return {"answer": answer}