<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Training a POS Tagger and Dependency Parser for a Low-Resource Language (Tagalog)

This project trains a part-of-speech tagger and dependency parser for a
low-resource language such as Tagalog. We will be using the
[TRG](https://universaldependencies.org/treebanks/tl_trg/index.html) and
[Ugnayan](https://universaldependencies.org/treebanks/tl_ugnayan/index.html)
treebanks for this task. Since the number of sentences in each corpus is small,
we'll need to evaluate our model using [10-fold cross
validation](https://universaldependencies.org/release_checklist.html#data-split).
How to implement this split will be demonstrated in this project
(`scripts/kfold.py`). The cross validation results can be seen below.

### Monolingual evaluation

Consists of k-fold cross validation and inter-treebank evaluation.

**TRG Treebank**

|         | TOKEN_ACC | POS_ACC | MORPH_ACC | TAG_ACC | DEP_UAS | DEP_LAS |
|---------|-----------|---------|-----------|---------|---------|---------|
| 10-fold | 1.000     | 0.843   | 0.749     | 0.833   | 0.846   | 0.554   |
| Ugnayan | 0.997     | 0.563   | 0.364     | 0.538   | 0.472   | 0.240   |

**Ugnayan Treebank**

|         | TOKEN_ACC | POS_ACC | MORPH_ACC | TAG_ACC | DEP_UAS | DEP_LAS |
|---------|-----------|---------|-----------|---------|---------|---------|
| 10-fold | 0.998     | 0.819   | 0.995     | 0.810   | 0.667   | 0.409   |
| TRG     | 1.000     | 0.789   | 0.424     | 0.779   | 0.793   | 0.572   |

### Cross-lingual evaluation

Evaluating models trained from other typologically similar languages against
the two `tl` treebanks.

**TRG Treebank**

|           | TOKEN_ACC | POS_ACC | MORPH_ACC | TAG_ACC | DEP_UAS | DEP_LAS |
|-----------|-----------|---------|-----------|---------|---------|---------|
| id-gsd    | 1.000     | 0.374   | 0.320     | 0.000   | 0.342   | 0.151   |
| vi-vtb    | 1.000     | 0.306   | 0.423     | 0.000   | 0.309   | 0.143   |
| ro-rrt    | 0.999     | 0.392   | 0.198     | 0.000   | 0.304   | 0.098   |
| uk-iu     | 1.000     | 0.185   | 0.177     | 0.000   | 0.539   | 0.188   |
| ca-ancora | 0.999     | 0.284   | 0.057     | 0.015   | 0.261   | 0.081   |

**Ugnayan Treebank**

|           | TOKEN_ACC | POS_ACC | MORPH_ACC | TAG_ACC | DEP_UAS | DEP_LAS |
|-----------|-----------|---------|-----------|---------|---------|---------|
| id-gsd    | 0.997     | 0.310   | 0.803     | 0.000   | 0.251   | 0.058   |
| vi-vtb    | 0.997     | 0.256   | 0.986     | 0.000   | 0.199   | 0.049   |
| ro-rrt    | 0.992     | 0.332   | 0.275     | 0.000   | 0.279   | 0.085   |
| uk-iu     | 0.998     | 0.151   | 0.123     | 0.000   | 0.300   | 0.084   |
| ca-ancora | 0.994     | 0.267   | 0.301     | 0.025   | 0.242   | 0.041   |


## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `install` | Install dependencies |
| `preprocess-tl` | Convert the data to spaCy's format |
| `preprocess-foreign` | Convert foreign treebanks to spaCy's format |
| `split` | Split the raw corpus into train and dev datasets (80/20) |
| `train-tl` | Train UD_Tagalog-TRG and UD_Tagalog-Ugnayan |
| `train-foreign` | Train model from foreign treebanks |
| `evaluate-kfold` | Evaluate model using k-fold cross validation |
| `evaluate-treebank` | Evaluate the treebank model across each other |
| `evaluate-foreign-trg` | Evaluate foreign treebanks on the Tagalog TRG treebank |
| `evaluate-foreign-ugn` | Evaluate foreign treebanks on the Tagalog Ugnayan treebank |
| `package` | Package the trained models so it can be installed |
| `clean` | Remove intermediate files |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `monolingual` | `install` &rarr; `preprocess-tl` &rarr; `split` &rarr; `train-tl` &rarr; `evaluate-kfold` &rarr; `evaluate-treebank` |
| `crosslingual` | `install` &rarr; `preprocess-foreign` &rarr; `train-foreign` &rarr; `evaluate-foreign-trg` &rarr; `evaluate-foreign-ugn` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/UD_Tagalog-TRG` | Git | Treebank data for UD_Tagalog-TRG |
| `assets/UD_Tagalog-Ugnayan` | Git | Treebank data for UD_Tagalog-Ugnayan |
| `assets/UD_Indonesian-GSD` | Git | Treebank data for UD_Indonesian-GSD |
| `assets/UD_Ukrainian-IU` | Git | Treebank data for UD_Ukrainian-IU |
| `assets/UD_Vietnamese-VTB` | Git | Treebank data for UD_Vietnamese-VTB |
| `assets/UD_Romanian-RRT` | Git | Treebank data for UD_Romanian-RRT |
| `assets/UD_Catalan-AnCora` | Git | Treebank data for UD_Catalan-AnCora |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->