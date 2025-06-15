from fastapi import FastAPI
from app.models import UserInput, BotResponse
from app.ollama_client import call_mistral
from app.task_manager import TaskManager

app = FastAPI()
task_manager = TaskManager()

@app.post("/chat", response_model=BotResponse)
def chat_endpoint(user_input: UserInput):
    message = user_input.message.lower()

    if any(kw in message for kw in ["创建", "build", "添加", "新增"]):
        task_manager.build(message)
    elif any(kw in message for kw in ["删除", "删减", "delete"]):
        task_manager.delete(message)
    elif any(kw in message for kw in ["完成", "更新", "finish", "update"]):
        task_manager.update(message)

    tasks = task_manager.get_all()
    response = call_mistral(user_input.message, tasks)

    return BotResponse(reply=response, tasks=tasks)
