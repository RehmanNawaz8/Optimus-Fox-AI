# main.py

import os
import google.generativeai as genai
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_core.language_models import BaseLanguageModel
from langchain.llms.base import LLM
from typing import Any, List, Optional, ClassVar
from langchain_core.outputs import Generation

# ---------- STEP 1: Setup Gemini ----------
API_KEY = "AIzaSyBeG8aotddvne9doWE7NjHaPsvwDxd3kwY"  # Replace this with your actual Gemini API key
genai.configure(api_key=API_KEY)

# ---------- STEP 2: Define a LangChain-compatible Gemini Wrapper ----------
class GeminiLLM(LLM):
    model: ClassVar[str] = "models/gemini-1.5-pro"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response = genai.GenerativeModel(self.model).generate_content(prompt)
        return response.text

    @property
    def _llm_type(self) -> str:
        return "gemini"

# ---------- STEP 3: Load and Split PDF ----------
pdf_path = "snakes.pdf"
if not os.path.isfile(pdf_path):
    raise FileNotFoundError(f"PDF file not found at: {pdf_path}")

loader = PyPDFLoader(pdf_path)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

# ---------- STEP 4: Embed and Store in FAISS ----------
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(docs, embedding)

# ---------- STEP 5: Create Retriever ----------
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# ---------- STEP 6: Setup Gemini as LLM ----------
llm = GeminiLLM()

# ---------- STEP 7: Build RAG Chain ----------
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True
)

# ---------- STEP 8: Ask Questions ----------
while True:
    query = input("\n❓ Ask a question (or type 'exit'): ")
    if query.lower() == "exit":
        print("👋 Goodbye!")
        break

    result = rag_chain.invoke(query)

print("\n💬 Answer:", result['result'])

print("\n📚 Source Info:")
for i, doc in enumerate(result['source_documents']):
    print(f"--- Document {i+1} ---")
    print(f"Content: {doc.page_content[:200]}...")
    print(f"Metadata: {doc.metadata}")

