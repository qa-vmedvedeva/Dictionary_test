import pytest
@pytest.fixture
def added_word(api_client, request):
    create_payload = request.param["create"]
    updated_payload = request.param["update"]
    #add word
    response = api_client.post("/api/words", json=create_payload)
    assert response.status_code == 201

    word = response.json()
    word_id = word["id"]
    yield {
        "id": word_id,
        "create": create_payload,
        "update": updated_payload
    }

    api_client.delete(f"/api/words/{word['id']}")
@pytest.fixture
def invalid_word(api_client, request):
    create_payload = request.param["word"]

    yield create_payload

