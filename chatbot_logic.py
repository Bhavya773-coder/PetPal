import json

# Load knowledge base
with open("data/cat_knowledge_base.json", "r") as f:
    kb = json.load(f)

def get_bot_response(message):
    message = message.lower()

    # Medicines
    for med_name, info in kb["medicines"].items():
        if med_name.lower() in message:
            return f"**{med_name}**: {info['use']} \n\n**Dosage**: {info['dosage']} \n**Precautions**: {info['precautions']}"

    # Feeding
    if "feed" in message or "food" in message:
        if "kitten" in message:
            return f"Kitten Feeding Tip: {kb['feeding']['kitten']}"
        elif "senior" in message:
            return f"Senior Cat Feeding Tip: {kb['feeding']['senior']}"
        else:
            return f"Adult Cat Feeding Tip: {kb['feeding']['adult']}"

    # Grooming
    if "groom" in message or "nail" in message or "bath" in message or "brush" in message:
        return (
            f"Grooming Tips:\n"
            f"- Brushing: {kb['grooming']['brushing']}\n"
            f"- Bathing: {kb['grooming']['bathing']}\n"
            f"- Nail Trimming: {kb['grooming']['nail_trim']}"
        )

    # Illness or symptoms
    for symptom, advice in kb["illness_signs"].items():
        if symptom in message:
            return f"If your cat is experiencing {symptom}, {advice}"

    # Toxic foods
    if "toxic" in message or "not eat" in message or "dangerous food" in message:
        return "These foods are toxic to cats:\n" + ", ".join(kb["toxic_foods"])

    # FAQs
    for question, answer in kb["faq"].items():
        if question in message:
            return answer

    return "I'm still learning! Try asking about cat medicine, feeding, grooming, or illnesses."
