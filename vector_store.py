from langchain_google_genai import GoogleGenerativeAIEmbeddings
from utils import env

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=env.GEMINI_API_KEY)

def get_vector_store(persist_dir=env.CHROMA_PERSIST_DIR):
    from langchain.vectorstores import Chroma
    return Chroma(persist_directory=persist_dir, embedding_function=embeddings)