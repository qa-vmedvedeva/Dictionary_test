import pytest
from fixtures.words_fixture import added_word, invalid_word
from data.words import VALID_WORDS, INVALID_WORDS

@pytest.mark.parametrize(
    "added_word",
    VALID_WORDS,
    indirect=True,
    ids=lambda w: w["create"]["word"]
)
#add word
def test_add_word(added_word, api_client):
    word_id = added_word["id"]

    #find added word
    response = api_client.get(f"/api/words/{word_id}")
    assert response.status_code == 200
    assert added_word["create"]["word"] == response.json()["word"]
    assert added_word["create"]["translation"] == response.json()["translation"]

    #edit added word
    response = api_client.put(f"/api/words/{word_id}", added_word["update"])
    assert response.status_code == 200

    response = api_client.get(f"/api/words/{word_id}")
    assert response.json()["word"] == added_word["update"]["word"]
    assert response.json()["translation"] == added_word["update"]["translation"]
    #delete word
    response = api_client.delete(f"/api/words/{word_id}")
    assert response.status_code in(200, 204)
    response = api_client.get(f"/api/words/{word_id}")
    assert response.status_code == 404
