"""Convert entity annotation from into spaCy v3 .spacy format."""
import srsly
import typer
import warnings
from pathlib import Path

import spacy
from spacy.tokens import DocBin
import random


def convert(lang: str, input_path: Path, output_train: Path, output_valid: Path):
    random.seed(42)
    nlp = spacy.blank(lang)
    db_train = DocBin()
    db_valid = DocBin()
    for ex in srsly.read_jsonl(input_path):
        doc = nlp.make_doc(ex['text'])
        ents = []
        for s in ex.get("spans", []):
            span = doc.char_span(s['start'], s['end'], label=s['label'])
            ents.append(span)
        doc.ents = ents
        if random.random() < 0.3:
            db_train.add(doc)
        else:
            db_valid.add(doc)
    db_train.to_disk(output_train)
    db_valid.to_disk(output_valid)


if __name__ == "__main__":
    typer.run(convert)