import json

# Load knowledge base
with open("data/cat_knowledge_base.json", "r") as f:
    kb = json.load(f)

def get_bot_response(message):
    message = message.lower()

    # Medicines
    for med in kb.get("medicines", []):
        if med["name"].lower() in message:
            return f"**{med['name']}**: {med['info']}"

    # Vaccines
    for vac in kb.get("vaccines", []):
        if vac["name"].lower() in message:
            return f"**{vac['name']} Vaccine**: {vac['info']}"

    # Diseases
    for disease in kb.get("diseases", []):
        if disease["name"].lower() in message:
            return f"**{disease['name']}**: {disease['info']}"

    # Behavior
    for behavior in kb.get("behavior", []):
        if behavior["name"].lower() in message:
            return f"**Behavior Tip - {behavior['name']}**: {behavior['info']}"

    # Diet
    for diet in kb.get("diet", []):
        if diet["name"].lower() in message:
            return f"**Diet for {diet['name']} Cats**: {diet['info']}"

    # Emergency
    for emergency in kb.get("emergency", []):
        if emergency["name"].lower() in message:
            return f"**Emergency - {emergency['name']}**: {emergency['info']}"

    # FAQs (keyword matching)
    for faq in kb.get("faq", []):
        question = faq["question"].lower()
        if question in message or any(word in message for word in question.split()):
            return faq["answer"]

    return "I'm still learning! Try asking about medicines, vaccines, diseases, diet, behavior, or emergencies for your cat."
