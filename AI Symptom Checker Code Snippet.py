import spacy
nlp = spacy.load("en_core_web_sm")
def analyze_symptom(text):
    doc = nlp(text)
    if "fever" in text.lower():
        return "You may have a fever. Stay hydrated and rest."
    elif "headache" in text.lower():
        return "You may be experiencing a headache. Rest and stay calm."
    else:
        return "Please consult a doctor for a detailed diagnosis."
