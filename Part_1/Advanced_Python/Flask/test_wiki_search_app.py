import pytest
from wiki_search_app import app, parse_wiki_search_output



FIRST_PYTHON_NETWORK_RESULT = [
        "Python (programming language)",
        "/wiki/Python_(programming_language)",
        "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy "
        "emphasizes code readability with its notable",
    ]

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_can_proxy_request_to_wiki(client):
    app_response = client.get("/api/search?query=python network")
    assert 200 == app_response.status_code

    assert app_response.is_json
    json_response = app_response.get_json()
    assert FIRST_PYTHON_NETWORK_RESULT == json_response["documents"][0]
    assert any("NetworkX" in document[2] for document in json_response["documents"])


def test_can_parse_wiki_search_output():
    with open("wikipedia_python_network.html") as fin:
        wiki_search_output_html = fin.read()
    documents = parse_wiki_search_output(wiki_search_output_html)
    assert 20 == len(documents)
    assert FIRST_PYTHON_NETWORK_RESULT[0] == documents[0][0]
