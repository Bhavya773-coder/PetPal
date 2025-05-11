from utils.semantic_search import load_knowledge, create_embeddings, save_model_and_index

data = load_knowledge("data/cat_knowledge_base.json")
model, embeddings = create_embeddings(data)
save_model_and_index(model, embeddings, data)
