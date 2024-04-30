import srsly
from gliner import GLiNER

model = GLiNER.from_pretrained("urchade/gliner_base")

text = """
Yeah, that sounds really cool. What machine learning libraries does it support? Is it just scikit-learn? Does it do like, Keras, PyTorch, spaCy or any others?
"""

labels = ["python-tool"]

for line in srsly.read_jsonl("data/lines.jsonl"):
    entities = model.predict_entities(line['text'], labels)
    for entity in entities:
        print(entity["text"], "=>", entity["label"], entity)
