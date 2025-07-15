from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage




load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


def get_llm_response(question: str) -> str:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    messages = [
        HumanMessage(content=question),
    ]

    response = llm.invoke(messages)
    return response.content