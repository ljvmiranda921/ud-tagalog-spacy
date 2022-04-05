import random
from pathlib import Path
from typing import List, Optional

import spacy
import typer
from spacy.tokens import Doc, DocBin
from wasabi import msg


def main(infile: Path, outdir: Path, seed: Optional[int] = 42):
    nlp = spacy.blank("tl")
    doc_bin = DocBin().from_disk(infile)
    docs = list(doc_bin.get_docs(nlp.vocab))

    msg.info("Splitting data into train (80) and test (20) partitions")
    if seed:
        msg.info(f"Setting random seed to {seed}")
        random.seed(seed)

    random.shuffle(docs)
    train_size = int(0.8 * len(docs))

    train_data: List[Doc] = docs[:train_size]
    dev_data: List[Doc] = docs[train_size:]
    msg.text(f"Train size: {len(train_data)}, dev size: {len(dev_data)}")

    msg.info(f"Saving to {outdir}")
    train_doc_bin = DocBin(docs=train_data)
    train_doc_bin.to_disk(outdir / "train.spacy")
    dev_doc_bin = DocBin(docs=dev_data)
    dev_doc_bin.to_disk(outdir / "dev.spacy")


if __name__ == "__main__":
    typer.run(main)
