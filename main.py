import argparse
import os
from dotenv import load_dotenv

from graph import build_graph
from nodes import llm

def parse_args():
    parser = argparse.ArgumentParser(description="LangGraph Reflection Demo")
    parser.add_argument("question", type=str, help="The question to answer")
    parser.add_argument("--max-rounds", type=int, default=2, help="Maximum number of rewrite attempts")
    parser.add_argument("--model", type=str, default="gpt-3.5-turbo", help="LLM model name")
    return parser.parse_args()

def main():
    load_dotenv()
    args = parse_args()

    # Configure LLM
    llm.model = args.model

    graph = build_graph()
    initial_state = {
        "question": args.question,
        "draft": "",
        "critique": "",
        "verdict": "",
        "round": 1,
        "max_rounds": args.max_rounds,
    }

    result = graph.invoke(initial_state)

    print("\n=== Final Result ===")
    print(f"Draft:\n{result['draft']}\n")
    print(f"Verdict: {result['verdict']}")
    print(f"Critique:\n{result['critique']}\n")
    print(f"Round: {result['round']}")

if __name__ == "__main__":
    main()
