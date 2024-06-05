import spacy
import scipy
# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# List of garden path sentences
gardenpathSentences = [
    "The old man the boat.",
    "The horse raced past the barn fell.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Tokenisation and Named Entity Recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print('_'*8)
    print(f"Sentence: {sentence}")
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    if entities:
        print("Entities:", entities)
    else:
        print("No named entities found.")

    # Print explanation of entity
    for ent in doc.ents:
        explanation = spacy.explain(ent.label_)
        print(f'explanation: {explanation}')


