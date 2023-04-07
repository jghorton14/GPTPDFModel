import os

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from langchain.chat_models import ChatOpenAI

# https://platform.openai.com/account/api-keys
os.environ['OPENAI_API_KEY'] = 'SECRET_KEY'

if __name__ == '__main__':
    documents = SimpleDirectoryReader('data').load_data()

    llm_predictor = LLMPredictor(llm=ChatOpenAI(
        temperature=0, model_name="gpt-3.5-turbo"))
    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor, chunk_size_limit=512)

    index = GPTSimpleVectorIndex.from_documents(
        documents, service_context=service_context)

    while True:
        prompt = input("Type prompt...")
        response = index.query(
            prompt, 
            service_context=service_context,
            similarity_top_k=3
        )
        print(response)
