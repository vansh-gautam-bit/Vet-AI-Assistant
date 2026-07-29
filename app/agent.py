from langgraph.prebuilt import create_react_agent

from app.prompts.system_prompt import SYSTEM_PROMPT
from app.services.llm import llm
from app.tools import TOOLS

agent = create_react_agent(
    model=llm,
    tools=TOOLS,
    prompt=SYSTEM_PROMPT,
)