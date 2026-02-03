import pytest
from data.words import INVALID_WORDS
from fixtures.words_fixture import invalid_word, added_word
@pytest.mark.parametrize(
    "invalid_word",
    INVALID_WORDS,
    indirect=True,
    ids=lambda w: w["word"]
)

def test_post_word_not_found(invalid_word, api_client):
    print(invalid_word)
    response = api_client.post(f"/api/words/", invalid_word)
    assert response.status_code in (400,404)
    print(response.status_code)


def test_get_word_not_found(api_client):
    response = api_client.get(f"/api/words/100000")
    assert response.status_code == 404

def test_delete_word(api_client):
    word_id = 100000
    response = api_client.get(f"/api/words/{word_id}")
    assert response.status_code == 404
