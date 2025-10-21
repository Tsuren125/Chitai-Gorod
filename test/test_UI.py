from page.MainPage import MainPage
from data.data import TEST_PHONE_NUMBER, TEST_NAME
import allure


@allure.title("Тестирование поиска книг на сайте по полному названию")
@allure.description("Тест проверяет возможность найти книги по полному названию")
@allure.feature("Онлайн-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_search(driver):
    with allure.step("Подтверждение местонахождения пользователя"):
        main_page = MainPage(driver)
        main_page.confirm_location()
    with allure.step("Закрытие всплывающего окна, предлагающего войти или зарегистрироваться"):
        main_page.enter_or_registrate()
    with allure.step("Принятие cookie"):
        main_page.confirm_cookie()
    with allure.step("Поиск книги по полному названию"):
        main_page.search_full_name(TEST_NAME)
    with allure.step("Проверка введенного названия с названием найденных книг"):
        title = main_page.found_books()
    assert TEST_NAME in title


@allure.title("Проверка неактивности кнопки "'Получить код')
@allure.description("Тест проверяет невозможность нажатия на кнопку 'Получить код',"
                    "если не введен номер телефона")
@allure.feature("Онлайн-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_button_disabled_before_phone_input(driver):
    with allure.step("Подтверждение местонахождения пользователя"):
        main_page = MainPage(driver)
        main_page.confirm_location()
    with allure.step("Закрытие всплывающего окна, предлагающего войти или зарегистрироваться"):
        main_page.enter_or_registrate()
    with allure.step("Принятие cookie"):
        main_page.confirm_cookie()
    with allure.step("Открытие окна авторизации"):
        main_page.open_authorization_window()
    with allure.step("Проверка неактивности кнопки 'Получить код'"):
        button = main_page.get_button()
        print("Текст кнопки:", button.text)
        print("Атрибут 'disabled':", button.get_attribute("disabled"))
        print("Атрибут 'class':", button.get_attribute("class"))
    assert not button.is_enabled()


@allure.title("Проверка корректного ввода номера телефона")
@allure.description("Тест проверяет, что номер телефона вводится корректно")
@allure.feature("Онлайн-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_insert_phone_number(driver):
    with allure.step("Подтверждение местонахождения пользователя"):
        main_page = MainPage(driver)
        main_page.confirm_location()
    with allure.step("Закрытие всплывающего окна, предлагающего войти или зарегистрироваться"):
        main_page.enter_or_registrate()
    with allure.step("Принятие cookie"):
        main_page.confirm_cookie()
    with allure.step("Открытие окна авторизации"):
        main_page.open_authorization_window()
    with allure.step("ввод номера телефона для возможности получить код"):
        phone_number = TEST_PHONE_NUMBER
    with allure.step("Проверить корректность ввода номера телефона"):
        received_phone_number = main_page.insert_phone_number(phone_number)
    assert received_phone_number == phone_number


@allure.title("Проверка количества товара в корзине, после добавления 1 книги")
@allure.description("Тест проверяет, что после одного нажатия на кнопку 'Купить,"
                    "В корзине только один товар")
@allure.feature("Онлайн-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_count_products_after_one_add(driver):
    with allure.step("Подтверждение местонахождения пользователя"):
        main_page = MainPage(driver)
        main_page.confirm_location()
    with allure.step("Закрытие всплывающего окна, предлагающего войти или зарегистрироваться"):
        main_page.enter_or_registrate()
    with allure.step("Принятие cookie"):
        main_page.confirm_cookie()
    with allure.step("Поиск книги по полному названию"):
        main_page.search_full_name(TEST_NAME)
    with allure.step("Добавление книги в корзину"):
        main_page.add_to_cart()
    with allure.step("Переход в корзину"):
        main_page.go_to_cart()
    with allure.step("Получить количество товаров в корзине"):
        count = main_page.get_count_products()
    assert count == 1


@allure.title("Проверка очистки корзины")
@allure.description("Тест проверяет, что после нажатия на кнопку 'Очистить корзину"
                    "товары удаляются")
@allure.feature("Онлайн-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_clear_cart(driver):
    with allure.step("Подтверждение местонахождения пользователя"):
        main_page = MainPage(driver)
        main_page.confirm_location()
    with allure.step("Закрытие всплывающего окна, предлагающего войти или зарегистрироваться"):
        main_page.enter_or_registrate()
    with allure.step("Поиск книги по полному названию"):
        main_page.search_full_name(TEST_NAME)
    with allure.step("Добавление книги в корзину"):
        main_page.add_to_cart()
    with allure.step("Переход в корзину"):
        main_page.go_to_cart()
    with allure.step("Очистить корзину"):
        main_page.clear_cart()
    with allure.step("Принятие cookie"):
        main_page.confirm_cookie()
    with allure.step("Проверить, что корзина очищена"):
        info = main_page.get_information()
    assert "Корзина очищена" in info
