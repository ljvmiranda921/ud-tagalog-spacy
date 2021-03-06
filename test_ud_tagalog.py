from pathlib import Path

import pytest

from spacy.cli.project.assets import project_assets
from spacy.cli.project.run import project_run


def test_ud_tagalog_project():
    root = Path(__file__).parent
    project_assets(root)
    project_run(root, "monolingual", capture=True)
    project_run(root, "crosslingual", capture=True)
