from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
chat_history = [SystemMessage(content='You are a helpful assistant')]


model = ChatHuggingFace(llm=llm)

while True:
    user_input = input("You:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ['exit', 'quit']:
        break
    elif user_input:
        response = model.invoke(chat_history)
        chat_history.append(AIMessage(content=response.content))
        print("Bot:", response.content)
    
print(chat_history)