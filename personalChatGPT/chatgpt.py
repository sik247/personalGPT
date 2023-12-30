import os
import sys
import logging

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

import constants

# Configure logging to write to both console and a log file
log_file_path = "output.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Constants
EXIT_COMMANDS = ['quit', 'q', 'exit']

def load_data(data_path):
    """
    Determine the appropriate loader based on the file type.
    Supports loading from text files or PDFs.
    """
    _, extension = os.path.splitext(data_path.lower())

    if os.path.exists(data_path):
        if os.path.isdir(data_path):
            loader = DirectoryLoader(data_path)
        elif extension == '.txt':
            loader = TextLoader(data_path)
        else:
            print(f"Unsupported file type: {extension}")
            sys.exit(1)
    else:
        print(f"Data file '{data_path}' not found.")
        sys.exit(1)

    return loader

def main():
    os.environ["OPENAI_API_KEY"] = constants.APIKEY

    # Enable to save to disk & reuse the model (for repeated queries on the same data)
    PERSIST = False

    query = None
    if len(sys.argv) > 1:
        query = sys.argv[1]

    if PERSIST and os.path.exists("persist"):
        logger.info("Reusing index...\n")
        vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
        index = VectorStoreIndexWrapper(vectorstore=vectorstore)
    else:
        # Specify the directory path here
        data_path = "data/data.txt"
        loader = load_data(data_path)

        if PERSIST:
            index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory": "persist"}).from_loaders([loader])
        else:
            index = VectorstoreIndexCreator().from_loaders([loader])

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo"),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    chat_history = []
    while True:
        if not query:
            query = input("Prompt: ")
        if query.lower() in EXIT_COMMANDS:
            sys.exit()

        try:
            result = chain({"question": query, "chat_history": chat_history})
            print(result['answer'])
            chat_history.append((query, result['answer']))
        except Exception as e:
            logger.error(f"An error occurred: {e}")

        query = None

if __name__ == "__main__":
    main()
