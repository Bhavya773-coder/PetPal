from sentence_transformers import SentenceTransformer
import faiss
import json
import os
import pickle

def load_knowledge(file_path):
    with open(file_path, 'r') as f:
        kb = json.load(f)
    data = []
    for category in kb.values():
        for item in category:
            data.append(item["info"])
    return data

def create_embeddings(data, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(data, show_progress_bar=True)
    return model, embeddings

def save_model_and_index(model, embeddings, data):
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    os.makedirs("embeddings", exist_ok=True)
    os.makedirs("data/faiss_index", exist_ok=True)
    faiss.write_index(index, "data/faiss_index/petpal.index")
    with open("embeddings/embedder.pkl", "wb") as f:
        pickle.dump((model, data), f)
