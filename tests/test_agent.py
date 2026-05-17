"""Tests for the Agent class."""

from __future__ import annotations

import pytest

from assistant_agent import Agent, __version__


def test_version_is_set() -> None:
    assert __version__ == "0.1.0"


def test_agent_default_response() -> None:
    agent = Agent(name="Rose")
    reply = agent.respond("halo")
    assert reply == "[Rose] received: halo"


def test_register_and_call_tool() -> None:
    agent = Agent()

    def add(a: int, b: int) -> int:
        return a + b

    agent.register_tool("add", add)
    assert agent.call_tool("add", 2, 3) == 5


def test_register_duplicate_tool_raises() -> None:
    agent = Agent()
    agent.register_tool("noop", lambda: None)

    with pytest.raises(ValueError, match="already registered"):
        agent.register_tool("noop", lambda: None)


def test_call_unknown_tool_raises() -> None:
    agent = Agent()

    with pytest.raises(KeyError, match="Unknown tool"):
        agent.call_tool("missing")
