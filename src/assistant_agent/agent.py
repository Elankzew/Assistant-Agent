"""Core Agent abstraction.

The Agent is intentionally minimal — it accepts a name, a system prompt,
and a list of tools (callables). Real LLM integration (OpenAI, Anthropic,
local models, etc.) is meant to be plugged in by subclassing or by
wiring the `respond` method to a model client.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

ToolFn = Callable[..., Any]


@dataclass
class Agent:
    """A minimal assistant agent.

    Attributes:
        name: Human-friendly identifier for the agent.
        system_prompt: Instruction text describing the agent's role.
        tools: Mapping of tool name -> callable. Tools are arbitrary
            Python functions the agent can be asked to invoke by name.
    """

    name: str = "Assistant"
    system_prompt: str = "You are a helpful assistant."
    tools: dict[str, ToolFn] = field(default_factory=dict)

    def register_tool(self, name: str, fn: ToolFn) -> None:
        """Register a callable under ``name``.

        Raises:
            ValueError: If a tool with the same name already exists.
        """
        if name in self.tools:
            raise ValueError(f"Tool already registered: {name}")
        self.tools[name] = fn

    def call_tool(self, name: str, *args: Any, **kwargs: Any) -> Any:
        """Invoke a registered tool by name."""
        if name not in self.tools:
            raise KeyError(f"Unknown tool: {name}")
        return self.tools[name](*args, **kwargs)

    def respond(self, message: str) -> str:
        """Generate a response to ``message``.

        This default implementation is an echo stub. Subclasses or callers
        should replace it with a real model call (OpenAI, Anthropic, etc.).
        """
        return f"[{self.name}] received: {message}"
