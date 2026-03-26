import pytest
from data.words import INVALID_WORDS, VALID_WORDS
from fixtures.words_fixture import invalid_word, added_word
@pytest.mark.parametrize(
    "invalid_word",
    INVALID_WORDS,
    indirect=True,
    ids=lambda w: w["word"]
)
def test_post_word_not_found(invalid_word, api_client):
    response = api_client.post(f"/api/words/", invalid_word)
    assert response.status_code in (400,404)

@pytest.mark.parametrize(
    "added_word",
    VALID_WORDS,
    indirect=True,
    ids=lambda w: w["create"]["word"]
)
def test_put_word_not_found(api_client, added_word):
    response = api_client.put(f"/api/words/10000000", added_word["update"])
    assert response.status_code == 404

def test_get_word_not_found(api_client):
    response = api_client.get(f"/api/words/100000")
    assert response.status_code == 404

def test_delete_word(api_client):
    word_id = 100000
    response = api_client.get(f"/api/words/{word_id}")
    assert response.status_code == 404
