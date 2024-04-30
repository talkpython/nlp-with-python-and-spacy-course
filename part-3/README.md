<!-- WEASEL: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 Weasel Project: Detecting techtools from the Python Bytes podcast.

This project contain a demo of a spaCy pipeline to detect programming tools and Python packages from podcast transcripts.

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[Weasel documentation](https://github.com/explosion/weasel).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`weasel run [name]`](https://github.com/explosion/weasel/tree/main/docs/cli.md#rocket-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `index` | Index the raw data so that a Prodigy recipe can easily search through it. |
| `annot-search` | Use a searching trick to annotate |
| `annot-model` | Use a model trick to annotate |
| `annot-export` | Get annotations out of Prodigy |
| `convert` | Convert annotations to spaCy format. |
| `config` | Create a configuration file for training. |
| `train` | Train a named entity recognition model |
| `package` | Package the trained model so it can be installed |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`weasel run [name]`](https://github.com/explosion/weasel/tree/main/docs/cli.md#rocket-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `convert` &rarr; `config` &rarr; `train` &rarr; `package` |

<!-- WEASEL: AUTO-GENERATED DOCS END (do not remove) -->
