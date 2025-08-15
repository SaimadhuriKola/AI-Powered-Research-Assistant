from agent.langchain_agent import answer_question
import asyncio

def test_answer_question():
    question = "What is AI?"
    answer = asyncio.run(answer_question(question))
    assert isinstance(answer, str)