from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# llm = HuggingFacePipeline.from_model_id(
#     model_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     task ='text-generation',
#     pipeline_kwargs = dict(
#         temperature = 0.5,
#         max_new_tokens = 100
#     )
# )

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

#1 - Prompt - detailed report
template1 = PromptTemplate(template = "Write a detailed report on {topic}.",input_variables = ['topic'])
#2 - Prompt - summary
template2 = PromptTemplate(template = "Write a 5 line summary on the following text./n {text}",input_variables = ['text'])


parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser 

result = chain.invoke({'topic': 'black hole'})

print(result)


# prompt1 = template1.invoke({'topic': 'black hole'})

# result1 = model.invoke(prompt1)

# prompt2 = template2.invoke({'text': result1.content})

# result2 = model.invoke(prompt2)

# print(result2.content)

