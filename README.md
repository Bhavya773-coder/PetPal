# 🐾 PetPal – Your Pet's Virtual Companion

**PetPal** is a user-friendly chatbot app built with **Streamlit**, designed to assist pet owners—especially cat lovers—with health tracking, reminders, personalized care tips, and AI-powered responses trained on a pet care knowledge base.

---

## 🌟 Features

- 💬 **Smart Chatbot**  
  Ask questions about pet care, symptoms, diet, behavior, and more—powered by SentenceTransformers + FAISS.
  
- 📋 **Pet Profile Management**  
  Store details like name, breed, age, and health notes.

- 📊 **Health Tracker**  
  Track appetite, weight, stool quality, and health concerns.

- ⏰ **Reminders**  
  Set and view reminders for vaccinations, checkups, and medications.

- 🧠 **Pet Tips**  
  See randomized health and care tips every visit.

---

## 🧰 Tech Stack

- **Frontend**: Streamlit  
- **ML & NLP**: SentenceTransformer (`all-MiniLM-L6-v2`), FAISS  
- **Storage**: JSON, Pickle (`.pkl`)  
- **Embedding**: Semantic search via FAISS Index  

---

## 📁 Folder Structure

```
PetPal/
├── app.py                        # Main Streamlit app
├── embeddings/
│   └── embedder.pkl              # Model + Knowledge Base
├── data/
│   ├── cat_knowledge_base.json   # Pet care facts
│   └── faiss_index/
│       └── petpal.index          # FAISS vector index
├── assets/
│   └── pet_image.jpg             # Homepage image (optional)
```

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/PetPal.git
cd PetPal
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

> Or manually:
```bash
pip install streamlit sentence-transformers faiss-cpu
```

### 3. Create Knowledge Base

Edit `data/cat_knowledge_base.json` like this:

```json
{
  "knowledge_base": [
    "Cats need a balanced diet of protein and fiber.",
    "Vaccinate your kitten by 8 weeks of age.",
    "Clean litter boxes daily to avoid odor and bacteria."
  ]
}
```

### 4. Generate Embeddings & FAISS Index

Create a Python file `generate_embedder.py` (code provided separately) and run:

```bash
python generate_embedder.py
```

### 5. Launch the App

```bash
streamlit run app.py
```

---

## 🔍 Example Questions for Chatbot

- “What are common signs of illness in cats?”
- “How often should I clean my cat's litter box?”
- “What to do if my cat stops eating?”

---

## ✅ Optional Enhancements

- Add dog or multi-pet support by expanding the knowledge base.
- Connect reminders to system notifications or email.
- Add login to save multiple pet profiles.

---

## 👤 Author

Developed with ❤️ by Bhavya

---

## 📄 License

MIT License. Feel free to use and modify.
