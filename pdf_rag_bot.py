import pdfplumber
import faiss
import requests
import numpy as np
import streamlit as st

 
EURI_API_KEY = "euri-2b3c07b523bc64b29052f7abe729232e3e2b6ff8d98eda2165724f56be104e3a"
EURI_CHAT_URL = "https://api.euron.one/api/v1/euri/alpha/chat/completions"
EURI_EMBED_URL = "https://api.euron.one/api/v1/euri/alpha/embeddings"

conversation_memory = []

def extract_text_from_pdf(pdf_path):
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"
    return full_text

def split_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


def get_euri_embeddings(texts):
    headers = {
        "Authorization": f"Bearer {EURI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "text-embedding-3-small",
        "input": texts
    }
    res = requests.post(EURI_EMBED_URL, headers=headers, json=payload)
    return np.array([d["embedding"] for d in res.json()["data"]])

def build_vector_store(chunks):
    embeddings = get_euri_embeddings(chunks)
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(embeddings)
    return index, embeddings

def retrieve_context(question, chunks, index, embeddings, top_k=3):
    q_embed = get_euri_embeddings(question)[0]
    D, I = index.search(np.array([q_embed]), top_k)
    return "\n\n".join(chunks[i] for i in I[0])

