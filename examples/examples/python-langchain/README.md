# Python + LangChain

Example showing how to use Free-AI Gateway with the OpenAI Python SDK
and LangChain.

## Requirements

- Python 3.10+
- Free-AI Gateway running locally on port 3000

## Install

```bash
pip install -r requirements.txt
Run

Start Free-AI Gateway, then run:

python main.py

The example connects to:

http://localhost:3000/v1
Capability routing

The example demonstrates:

auto:text
auto:reasoning

These aliases allow the gateway to select a suitable provider based on
the requested capability.

LangChain streaming

The example also demonstrates streaming responses through LangChain's
ChatOpenAI integration.


Depois, no commit:

**Mensagem:**
```text
docs: add Python LangChain example README

Branch: docs/issue-19
