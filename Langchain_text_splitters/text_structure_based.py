from langchain.text_splitter import RecursiveCharacterTextSplitter 

text = """

This is a sample text that will be split into chunks based on character length. Long texts can be challenging to process in a single step, so splitting them into smaller, more manageable pieces can be beneficial.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

"""

splitter = RecursiveCharacterTextSplitter(
            chunk_size=50,
            chunk_overlap=0,

)

result = splitter.split_text(text)

print(len(result))
print(result)