import pytest
from src.tools import example_tool

def test_example_tool():
    assert example_tool(42) == 42
