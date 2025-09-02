
# branch_chain = RunnableBranch(
#     (lambda x: x.sentiment == 'positive', 
#         {"feedback": RunnableLambda(lambda x: x.feedback)} | prompt2 | model | parser),
#     (lambda x: x.sentiment == 'negative', 
#         {"feedback": RunnableLambda(lambda x: x.feedback)} | prompt3 | model | parser),
#     RunnableLambda(lambda x: "Could not determine sentiment")
# )

# chain = classifier_chain | branch_chain

# print(chain.invoke({'feedback': 'This is a beautiful phone'}))

