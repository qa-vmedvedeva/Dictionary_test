import pytest
import allure
from fixtures.words_fixture import added_word
from data.words import VALID_WORDS

@pytest.mark.parametrize(
    "added_word",
    VALID_WORDS,
    indirect=True,
    ids=lambda w: w["create"]["word"]
)
#add word
@allure.feature("Words API")
@allure.story("Create word")
@allure.title("Создание нового слова")
def test_add_word(added_word, api_client):
    word_id = added_word["id"]
    word = added_word["create"]["word"]
    translation = added_word["create"]["translation"]
    edited_word = added_word["update"]["word"]
    edited_translation = added_word["update"]["translation"]

    #find added word
    with allure.step("Find added word"):
        response = api_client.get(f"/api/words/{word_id}")
    with allure.step("Check if status is 200"):
        assert response.status_code == 200
    with allure.step("Check if word matches the resieved one"):
        assert word == response.json()["word"]
    with allure.step("Check if translation matches the resieved one"):
        assert translation == response.json()["translation"]
    #search full word
    with allure.step("search the word"):
        response = api_client.get(f"/api/words/search?q={word}")
    with allure.step("Check if status is 200"):
        assert response.status_code == 200
    with allure.step("Find word in response"):
        words = [item["word"] for item in response.json()]
        assert word in words
    with allure.step("Find translation in response"):
        translations = [item["translation"] for item in response.json()]
        assert translation in translations

    #edit added word
    with allure.step("Edit the word"):
        response = api_client.put(f"/api/words/{word_id}", added_word["update"])
    with allure.step("Check if status is 200"):
        assert response.status_code == 200

    with allure.step("Find edited word"):
        response = api_client.get(f"/api/words/{word_id}")
    with allure.step("Check if edited word matches the resieved one"):
        assert response.json()["word"] == edited_word
    with allure.step("Check if edited translation matches the resieved one"):
        assert response.json()["translation"] == edited_translation
    #delete word
    with allure.step("Delete the word"):
        response = api_client.delete(f"/api/words/{word_id}")
    with allure.step("Check if status is 200"):
        assert response.status_code in(200, 204)
    with allure.step("Check if deleted word does not exist"):
        response = api_client.get(f"/api/words/{word_id}")
        assert response.status_code == 404