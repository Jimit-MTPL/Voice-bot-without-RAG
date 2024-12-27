from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.chat_engine import SimpleChatEngine

def create_chat_engine():
        memory = ChatMemoryBuffer.from_defaults(token_limit=1500)
        chat_engine = SimpleChatEngine.from_defaults(memory=memory, system_prompt = """
            You are a professional AI Assistant receptionist working in one of the best restaurant called Taj.
            Based on your knowledge answer to user's question and help them making reservation of table at reataurant by asking user name, contact number and end conversation with greetings .
            If you don't know the answer, just say that you don't know, don't try to make up an answer.
            Provide concise and short answers, and don't chat with yourself!
        """)
        return chat_engine

def interact_with_llm(customer_query):
        print("Command: ", customer_query)
        chat_engine = create_chat_engine()
        AgentChatResponse = chat_engine.chat(customer_query)
        answer = AgentChatResponse.response
        return answer