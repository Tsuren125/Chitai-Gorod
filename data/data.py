BASE_URL = "https://www.chitai-gorod.ru/"
BASE_URL_API = "https://web-gate.chitai-gorod.ru/api/v2"
BASE_URL_SEARCH = BASE_URL_API + "/search/product"

HEADERS_PROJECT = {
        "Authorization": "Подставить свой токен авторизации",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    }

PARAMS_FULL_NAME = {
    "customerCityId": 213,
    "sortPreset": "relevance",
    "products[page]": 1,
    "products[per-page]": 60,

    "phrase": "Волшебник Изумрудного города"
}
PARAMS_ONE_WORD = {
    "customerCityId": 213,
    "sortPreset": "relevance",
    "products[page]": 1,

    "products[per-page]": 60,
    "phrase": "Волшебник Изумрудного города"
}
PARAMS_TWO_LETTERS = {
    "customerCityId": 213,
    "sortPreset": "relevance",
    "products[page]": 1,
    "products[per-page]": 60,
    "phrase": "Во"
}
PARAMS_ONE_LETTER = {
    "customerCityId": 213,
    "sortPreset": "relevance",
    "products[page]": 1,
    "products[per-page]": 60,
    "phrase": "В"
}
PARAMS_EMPTY = {
    "customerCityId": 213,
    "sortPreset": "relevance",
    "products[page]": 1,
    "products[per-page]": 60,
    "phrase": ""
}

TEST_PHONE_NUMBER = "+7 (916) 458-79-63"
TEST_NAME = "Волшебник Изумрудного города"
