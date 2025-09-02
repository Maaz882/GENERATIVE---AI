from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
 

text = """

This is a sample text that will be split into chunks based on character length. Long texts can be challenging to process in a single step, so splitting them into smaller, more manageable pieces can be beneficial.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

"""

splitter = CharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0,
    separator = ""
)

result = splitter.split_text(text)

print(result)