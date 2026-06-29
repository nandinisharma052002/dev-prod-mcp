from agent.graph import build_graph

print("Building Graph")

agent = build_graph()

print("Invoking agent")

for event in agent.stream(
    {
        "messages": [
            (
                "user",
                "Where is _resolve_workspace_path defined?"
            )
        ]
    },
    config={
        "recursion_limit": 30
    }
):
    print(event)
