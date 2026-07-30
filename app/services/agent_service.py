from app.agent import agent 

def chat(message: str): 
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": message,
                }
            ]
        }
    )

    return result["messages"][-1].content