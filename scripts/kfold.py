import random
import tempfile
import json
from pathlib import Path
from typing import List, Optional

import spacy
import typer
from spacy.tokens import Doc, DocBin
from spacy.training.loop import train as train_nlp
from spacy.training.corpus import Corpus
from spacy.training.initialize import init_nlp
from spacy.cli._util import show_validation_error
from spacy.util import load_config
from wasabi import msg

METRICS = ["pos_acc", "morph_acc", "tag_acc", "dep_uas", "dep_las"]


def chunk(l: List, n: int):
    """Split a list l into n chunks of fairly equal number of elements

    Source: https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
    """
    k, m = divmod(len(l), n)
    return (l[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)] for i in range(n))


def get_all_except(l: List, idx: int):
    """Get all elements of a list except a given index"""
    return l[:idx] + l[(idx + 1) :]


def flatten(l: List) -> List:
    """Flatten a list of lists"""
    return [item for sublist in l for item in sublist]


def main(
    corpus: Path,
    config_path: Path,
    n_folds: int = 10,
    seed: Optional[int] = None,
    shuffle: bool = False,
    output: Optional[Path] = None,
):
    nlp = spacy.blank("tl")
    doc_bin = DocBin().from_disk(corpus)
    docs = list(doc_bin.get_docs(nlp.vocab))

    if seed:
        random.seed(seed)
    if shuffle:
        random.shuffle(docs)

    folds = list(chunk(docs, n_folds))
    all_scores = {metric: [] for metric in METRICS}
    for idx, fold in enumerate(folds):
        dev = fold
        train = flatten(get_all_except(folds, idx=idx))
        msg.divider(f"Fold {idx+1}, train: {len(train)}, dev: {len(dev)}")

        # Save the train and test dataset into a temporary directory
        # then train within the context of that directory
        with tempfile.TemporaryDirectory() as tmpdir:

            msg.info("Preparing data for training")
            overrides = {
                "paths.train": str(Path(tmpdir) / "tmp_train.spacy"),
                "paths.dev": str(Path(tmpdir) / "tmp_dev.spacy"),
            }
            tmp_train_docbin = DocBin(docs=train)
            tmp_train_docbin.to_disk(overrides["paths.train"])
            tmp_dev_docbin = DocBin(docs=dev)
            tmp_dev_docbin.to_disk(overrides["paths.dev"])
            msg.good(
                f"Temp files at {overrides['paths.train']} and {overrides['paths.dev']}"
            )

            msg.info("Training model for the current fold")
            with show_validation_error(config_path, hint_fill=False):
                config = load_config(config_path, overrides, interpolate=False)
                nlp = init_nlp(config)

            nlp, _ = train_nlp(nlp, None)

            msg.info("Evaluating on the dev dataset")
            corpus = Corpus(overrides["paths.dev"], gold_preproc=False)
            dev_dataset = list(corpus(nlp))
            scores = nlp.evaluate(dev_dataset)

            # For our purposes, we'll only get the scores for the morphologizer,
            # dependency parser, and POS tagger
            for metric in METRICS:
                all_scores[metric].append(scores[metric])

    msg.info(f"Computing final {n_folds}-fold cross-validation score")
    avg_scores = {
        metric: sum(scores) / len(scores) for metric, scores in all_scores.items()
    }
    msg.table(avg_scores, header=("Metric", "Score"))
    if output:
        with output.open("w") as fp:
            json.dump(avg_scores, fp, indent=4)


if __name__ == "__main__":
    typer.run(main)
