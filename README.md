# LangGraph Reflection Demo

This project demonstrates a simple LangGraph that generates an answer to a question, reflects on it, and rewrites it if necessary. The graph loops until the answer is deemed satisfactory or a maximum number of rounds is reached.

## Features

- **Draft generation** – 5–10 sentence answer to a user question.
- **Reflection** – LLM critiques the draft and decides if it is acceptable.
- **Rewrite** – If the draft needs improvement, the LLM rewrites it based on the critique.
- **Loop control** – The process repeats until the answer is good enough or the maximum number of rounds is exceeded.
- **CLI** – Run the graph from the command line.

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/langgraph-reflection-demo.git
cd langgraph-reflection-demo

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Set your OpenAI API key
export OPENAI_API_KEY="your-openai-key"
```

> **Note**: If you prefer to use Ollama instead of OpenAI, replace `langchain-openai` with `langchain-ollama` in `requirements.txt` and adjust the LLM import in `nodes.py`.

## Usage

```bash
python main.py "Explain the theory of relativity in simple terms."
```

Optional arguments:

- `--max-rounds N` – Maximum number of rewrite attempts (default: 2).
- `--model MODEL` – LLM model name (default: `gpt-3.5-turbo`).

Example:

```bash
python main.py "What is quantum computing?" --max-rounds 3 --model gpt-4
```

The script will print:

```
Initial draft:
...

Reflection verdict: needs_revision
Critique:
...

Rewritten draft:
...

Final answer:
...
```

## Testing

Run the unit tests with:

```bash
pytest
```

The tests require a valid OpenAI API key set in the environment.

## License

MIT License
