from typing import TypedDict, Dict, Any
from langchain_community.llms import OpenAI
import re

# Global LLM instance
llm = OpenAI(temperature=0.7)

class ReflectState(TypedDict):
    question: str
    draft: str
    critique: str
    verdict: str
    round: int
    max_rounds: int

def draft_answer(state: ReflectState) -> ReflectState:
    prompt = (
        f"Answer the following question in 5–10 sentences:\n\n"
        f"Question: {state['question']}\n\n"
        f"Answer:"
    )
    answer = llm.invoke(prompt).strip()
    state["draft"] = answer
    return state

def reflect(state: ReflectState) -> ReflectState:
    prompt = (
        f"You are a critical reviewer. Evaluate the following draft answer.\n\n"
        f"Draft:\n{state['draft']}\n\n"
        f"Provide a verdict ('ok' or 'needs_revision') and 2–3 remarks.\n"
        f"Format:\n"
        f"Verdict: <ok|needs_revision>\n"
        f"Remarks:\n<remarks>"
    )
    response = llm.invoke(prompt).strip()
    # Parse verdict
    verdict_match = re.search(r"Verdict:\s*(\w+)", response, re.IGNORECASE)
    remarks_match = re.search(r"Remarks:\s*(.*)", response, re.DOTALL | re.IGNORECASE)
    verdict = verdict_match.group(1).lower() if verdict_match else "needs_revision"
    remarks = remarks_match.group(1).strip() if remarks_match else "No remarks provided."
    state["verdict"] = verdict
    state["critique"] = remarks
    return state

def rewrite(state: ReflectState) -> ReflectState:
    prompt = (
        f"Rewrite the following draft answer to address the remarks below.\n\n"
        f"Draft:\n{state['draft']}\n\n"
        f"Remarks:\n{state['critique']}\n\n"
        f"Provide the revised answer in 5–10 sentences."
    )
    revised = llm.invoke(prompt).strip()
    state["draft"] = revised
    state["round"] += 1
    return state
