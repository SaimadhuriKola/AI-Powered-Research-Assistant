from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from store.vector_store import get_vector_store
from utils import env

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=env.GEMINI_API_KEY, temperature=0.2)
vectorstore = get_vector_store()
retriever = vectorstore.as_retriever(search_kwargs={"k": 6})
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

async def answer_question(question: str) -> str:
    return qa_chain.run(question)