# Assistant Agent

A modular Python assistant agent scaffold — CLI, plugin-friendly tools, and a clean structure ready for real model integrations (OpenAI, Anthropic, local LLMs, etc.).

## Features

- Minimal `Agent` core with a tool registry
- `click`-based CLI (`assistant-agent chat "..."`)
- Pre-wired tooling: `pytest`, `ruff`, `mypy`
- GitHub Actions CI across Python 3.10 / 3.11 / 3.12

## Install (development)

```bash
git clone https://github.com/Elankzew/Assistant-Agent.git
cd Assistant-Agent

python -m venv venv
source venv/bin/activate

pip install -e ".[dev]"
```

## Usage

```bash
# Show version
assistant-agent --version

# Send a message to the agent
assistant-agent chat "halo, kabar?"

# Package info
assistant-agent info
```

Or directly in Python:

```python
from assistant_agent import Agent

agent = Agent(name="Rose")
print(agent.respond("halo"))
# [Rose] received: halo

# Register a tool
agent.register_tool("add", lambda a, b: a + b)
print(agent.call_tool("add", 2, 3))  # 5
```

## Project structure

```
Assistant-Agent/
├── src/assistant_agent/    # Package source
│   ├── __init__.py
│   ├── agent.py            # Core Agent class
│   └── cli.py              # CLI entrypoint
├── tests/                  # pytest suite
├── .github/workflows/      # CI
├── pyproject.toml          # Build + tool config
├── LICENSE                 # MIT
└── README.md
```

## Development

```bash
# Run the test suite
pytest

# Lint
ruff check .

# Auto-fix lint issues
ruff check --fix .

# Type-check
mypy src
```

## Roadmap

- [ ] Pluggable LLM backends (OpenAI, Anthropic, local)
- [ ] Async tool execution
- [ ] Memory / context store
- [ ] Streaming responses
- [ ] Plugin discovery via entry points

## License

MIT — see [LICENSE](./LICENSE).
