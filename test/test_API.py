from page.Api import Api
from data.data import (BASE_URL_SEARCH, PARAMS_FULL_NAME, PARAMS_ONE_WORD, PARAMS_TWO_LETTERS,
                       PARAMS_ONE_LETTER, PARAMS_EMPTY)
import allure

api = Api(BASE_URL_SEARCH)


@allure.title("Тестирование поиска книг по полному названию")
@allure.description("Тест проверяет возможность найти книги по полному названию")
@allure.feature("Онлайн-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_books_full_title():
    response = api.search(PARAMS_FULL_NAME)
    data = response.json()
    assert response.status_code == 200
    assert data["included"][0]["attributes"]["title"] == "Волшебник Изумрудного города"


@allure.title("Тестирование поиска книг по одному слову")
@allure.description("Тест проверяет возможность найти книги по одному слову")
@allure.feature("Онлайн-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_books_one_word():
    response = api.search(PARAMS_ONE_WORD)
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0


@allure.title("Тестирование поиска книг по двум символам")
@allure.description("Тест проверяет возможность найти книги по двум символам")
@allure.feature("Онлайн-магазин")
@allure.severity(allure.severity_level.MINOR)
def test_search_books_two_letters():
    response = api.search(PARAMS_TWO_LETTERS)
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0


@allure.title("Тестирование поиска книг по одному символу")
@allure.description("Тест проверяет возможность найти книги по одному символу")
@allure.feature("Онлайн-магазин")
@allure.severity(allure.severity_level.MINOR)
def test_search_books_one_letter():
    response = api.search(PARAMS_ONE_LETTER)
    data = response.json()
    assert response.status_code == 400
    assert data["errors"][0]["title"] == "Phrase должен содержать минимум 2 символа"


@allure.title("Тестирование поиска книг с пустым поиском")
@allure.description("Тест проверяет возможность найти книги без ввода данных")
@allure.feature("Онлайн-магазин")
@allure.severity(allure.severity_level.MINOR)
def test_search_books_empty():
    response = api.search(PARAMS_EMPTY)
    data = response.json()
    assert response.status_code == 400
    assert data["errors"][0]["title"] == "Phrase обязательное поле"
