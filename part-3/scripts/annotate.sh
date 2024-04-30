python -m prodigy ner.lunr.manual talk-python-ner blank:en data/lines.jsonl artifacts/index.gz.json --query "click" --allow-reset --labels techtool
python scripts/convert.py en data/annots.jsonl data
python -m spacy init config configs/base.cfg --pipeline ner --optimize efficiency --lang en --force

python -m spacy train configs/base.cfg --paths.train data/train.spacy --paths.dev data/valid.spacy --training.max_steps 2000 --output trained
python -m spacy package training/model-best packages --name ${vars.name} --version ${vars.version} --force t