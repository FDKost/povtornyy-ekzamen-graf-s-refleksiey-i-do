import os
import pytest
from graph import build_graph
from nodes import llm

@pytest.fixture(scope="module")
def graph():
    return build_graph()

@pytest.fixture(scope="module")
def initial_state():
    return {
        "question": "What is the capital of France?",
        "draft": "",
        "critique": "",
        "verdict": "",
        "round": 1,
        "max_rounds": 2,
    }

def test_draft_answer(graph, initial_state):
    result = graph.invoke(initial_state)
    assert result["draft"], "Draft should not be empty"
    assert result["round"] >= 1, "Round should be at least 1"

def test_reflection_and_rewrite(graph, initial_state):
    # Run until END
    result = graph.invoke(initial_state)
    # After graph finishes, verdict should be either ok or needs_revision
    assert result["verdict"] in ("ok", "needs_revision")
    # If needs_revision, round should be <= max_rounds
    if result["verdict"] == "needs_revision":
        assert result["round"] <= result["max_rounds"]
    # Draft should be updated
    assert result["draft"], "Draft should be updated"

def test_max_rounds(graph):
    state = {
        "question": "Explain quantum mechanics.",
        "draft": "",
        "critique": "",
        "verdict": "",
        "round": 1,
        "max_rounds": 1,
    }
    result = graph.invoke(state)
    # Should stop after one round
    assert result["round"] <= 1
    assert result["verdict"] in ("ok", "needs_revision")
