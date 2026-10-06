import pytest
from backend.tools.registry import BusinessTools

def test_vector_search():
    result = BusinessTools.vector_search("remote work")
    assert "RAG Search Results" in result

def test_database_lookup():
    result = BusinessTools.database_lookup("employee count")
    assert "Database Records" in result

def test_external_api_call():
    result = BusinessTools.external_api_call("https://api.example.com/sync")
    assert "API Response" in result