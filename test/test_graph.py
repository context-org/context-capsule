import json
from pathlib import Path

def test_graph_valid():
    graph_path = Path(__file__).parent.parent / "process_graph.json"
    with open(graph_path) as f:
        data = json.load(f)
    assert "graph" in data
    assert "nodes" in data
