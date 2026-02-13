import pytest
from fixtures.words_fixture import added_word
from data.words import VALID_WORDS

@pytest.mark.parametrize(
    "added_word",
    VALID_WORDS,
    indirect=True,
    ids=lambda w: w["create"]["word"]
)
#add word
def test_add_word(added_word, api_client):
    word_id = added_word["id"]
    word = added_word["create"]["word"]
    translation = added_word["create"]["translation"]
    edited_word = added_word["update"]["word"]
    edited_translation = added_word["update"]["translation"]

    #find added word
    response = api_client.get(f"/api/words/{word_id}")
    assert response.status_code == 200
    assert word == response.json()["word"]
    assert translation == response.json()["translation"]
    #search full word
    response = api_client.get(f"/api/words/search?q={word}")
    assert response.status_code == 200
    words = [item["word"] for item in response.json()]
    assert word in words
    translations = [item["translation"] for item in response.json()]
    assert translation in translations

    #edit added word
    response = api_client.put(f"/api/words/{word_id}", added_word["update"])
    assert response.status_code == 200

    response = api_client.get(f"/api/words/{word_id}")
    assert response.json()["word"] == edited_word
    assert response.json()["translation"] == edited_translation
    #delete word
    response = api_client.delete(f"/api/words/{word_id}")
    assert response.status_code in(200, 204)
    response = api_client.get(f"/api/words/{word_id}")
    assert response.status_code == 404
