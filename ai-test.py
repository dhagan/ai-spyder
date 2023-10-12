# Input files
# You can take many text files and store them in a directory on your local machine. I’ve grabbed input data from https://essaypro.com/blog/essay-samples and created 5 text files. My files are all about the ‘Cause And Effect Of Homelessness’ and are placed in a directory named Store.

# Import Required Packages
# As we are using Python, let’s go ahead and import the required packages.

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
#from langchain.document_loaders import DirectoryLoader
#import magic
import os
#import nltk
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers.pdf import PyPDFParser

# If you do not have the above packages installed on your machine, please install these packages before importing.

# nltk.download('averaged_perceptron_tagger')
# pip install langchain
# pip install openai
# pip install chromadb
# pip install unstructured
# pip install beautifulsoup4
# pip install python-magic-bin

# Once the required packages are imported, we need to get the OpenAI API key.

# Generating an OpenAI API Key
# To get the OpenAI key, go to https://openai.com/, login and then grab the keys using highlighted way.

# Use Your Own Files To Get Response From GPT like ChatGPT

# Once you get the key, set that inside an environment variable(I’m using Windows).

os.environ["OPENAI_API_KEY"] = "YOUR_KEY"

# Load Input Data
# To load our text files, we need to instantiate DirectoryLoader, and that can be done as shown below,

# loader = DirectoryLoader('Store', glob='**/*.txt')


# Import other parsers as needed

loaders = {
    '.pdf': GenericLoader.from_filesystem(
        path="./CarbonCashback",
        glob="**/*.pdf",
        parser=PyPDFParser(),
        show_progress=True
    ),
    # Add other file types and their respective loaders here
}

docs = []
for loader in loaders.values():
    docs.extend(loader.load())


# docs = loader.load()

# In the above code, glob must be mentioned to pick only the text files. This is particularly useful when your input directory contains a mix of different-different types of files.

# Split Data
# As input data could be very long, we need to split our data into small chunks, and here I’m taking chunk size as 1000.

char_text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
doc_texts = char_text_splitter.split_documents(docs)

# After splitting, this is how the text looks like,

# Use Your Own Files To Get Response From GPT like ChatGPT

# Create Vector Store
# Next, we need to create embeddings of it, which means we need to turn our data into a vector space. Let’s do this by instantiating the OpenAIEmbeddings object as shown below:

openAI_embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])
vStore = Chroma.from_documents(doc_texts, openAI_embeddings)

# Create Model
# Finally, time to create our model. This can be done by passing all the required parameters as shown below:

model = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=vStore)

# Once the model is ready, we are good to test it.

# Test Model
# To test the model, we need to ask some questions about it, and this can be done as shown below:

question = "What are the effects of homelessness"
model.run(question)