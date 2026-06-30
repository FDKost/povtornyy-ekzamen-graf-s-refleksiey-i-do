from langgraph.graph import StateGraph, END
from nodes import draft_answer, reflect, rewrite, ReflectState

def build_graph():
    graph = StateGraph(ReflectState)

    graph.add_node("draft_answer", draft_answer)
    graph.add_node("reflect", reflect)
    graph.add_node("rewrite", rewrite)

    def condition(state: ReflectState):
        if state["verdict"] == "ok":
            return "ok"
        if state["round"] >= state["max_rounds"]:
            return "maxed"
        return "needs_revision"

    graph.set_entry_point("draft_answer")
    graph.add_conditional_edges("reflect", condition, {
        "ok": END,
        "needs_revision": "rewrite",
        "maxed": END,
    })
    graph.add_edge("rewrite", "reflect")

    return graph.compile()
