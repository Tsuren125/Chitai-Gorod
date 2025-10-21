from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
import allure

base_url = "https://www.chitai-gorod.ru/"


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        """
        Конструктор класса MainPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """

    allure.step("Подтвердить местоположение пользователя в выпадающем списке")

    def confirm_location(self):
        # Ждем появления плашки "Ваш город - Москва?"
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(
                 (By.CSS_SELECTOR, 'div.header-location-popup')))

        # Ждем кликабельности кнопки "Да, я здесь"и нажимаем на нее
        confirm_button = WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Да, я здесь")]')))
        confirm_button.click()

    allure.step("Принять cookie")

    def confirm_cookie(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'chg-app-button__content') "
                           "and text()=' Понятно, закрыть ']"))).click()

    allure.step("Закрыть всплывающее окно, предлагающее войти или зарегистрироваться")

    def enter_or_registrate(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.popmechanic-main")))
        self.driver.find_element(
            By.CSS_SELECTOR, 'div.popmechanic-close').click()

    @allure.step("Найти книги по полному названию")
    def search_full_name(self, book_name):
        # Находим поисковую строку
        search_string = self.driver.find_element(
            By.CSS_SELECTOR, 'input[type="search"], input[placeholder*="поиск"], input.search-form__input')

        # Вводим название книги и нажимаем enter
        search_string.send_keys(book_name)
        search_string.send_keys(Keys.RETURN)

        self.driver.implicitly_wait(3)

    @allure.step("Получить названия найденных книг")
    def found_books(self):
        books = self.driver.find_elements(By.CSS_SELECTOR, "div.app-catalog__content")
        if books:
            title = books[0].find_element(By.CSS_SELECTOR, "a.product-card__title").text
            return title
        return None  # Если книг нет

    @allure.step("Открыть окно авторизации на главной странице через кнопку 'Войти'")
    def open_authorization_window(self):
        # Ждем кликабельности кнопки "Войти"
        authorize = WebDriverWait(self.driver, 10).until(
              EC.element_to_be_clickable(
                  (By.CSS_SELECTOR, 'span[class="header-controls__text"]')))
        self.driver.implicitly_wait(5)
        authorize.click()
        # Ждем появления формы авторизации
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'tid-form')))

    @allure.step("Проверить возможность ввода номера телефона")
    def insert_phone_number(self, phone_number):
        # Ждем кликабельности поля ввода номера телефона
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "tid-input")))
        phone_input = self.driver.find_element(By.ID, "tid-input")
        # Очистить строку ввода номера телефона
        phone_input.clear()
        # Ввести номер телефона
        phone_input.send_keys(phone_number)
        # Вернуть значение атрибута "value"
        return phone_input.get_attribute("value")

    @allure.step("Найти кнопку 'Получить код'")
    def get_button(self):
        button = self.driver.find_element(By.CSS_SELECTOR, 'button.chg-app-button[disabled]')
        return button

    @allure.step("Добавить книгу в корзину")
    def add_to_cart(self):
        # Ожидаем появление кнопки "Купить"
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "button.product-buttons__main-action[aria-label='false']")))
        self.driver.implicitly_wait(10)
        # Нажимаем на кнопку "Купить"
        buy_buttons = self.driver.find_elements(
            By.CSS_SELECTOR, "button.product-buttons__main-action[aria-label='false']")
        self.driver.execute_script("arguments[0].click();", buy_buttons[0])

    @allure.step("Перейти на страницу 'Корзина'")
    def go_to_cart(self):
        # Принудительно обновляем страницу, потому что иногда подвисает окно поиска,
        # которое не дает перейти в корзину
        self.driver.refresh()
        # Нажимаем на картинку "Корзина"
        cart_button = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Корзина"]')
        self.driver.execute_script("arguments[0].click();", cart_button)

    @allure.step("Получить количество товаров в корзине")
    def get_count_products(self):
        # Ждем появления элемента с текстом "1 товар"
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span.cart-page__title--append")))

        # Получаем весь текст из элемента
        total_text = element.text

        # Извлекаем первое значение из текста
        count = total_text.split()[0]  # Берем первое слово и преобразуем в число
        return int(count)

    @allure.step("Очистить корзину")
    def clear_cart(self):
        # Ожидаем появление всей плашки со словами "Корзина" и "Очистить корзину"
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-page__head-content")))
        # Ожидаем кликабельности предыдущего элемента
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-page__head-content")))
        self.driver.implicitly_wait(4)

        # Находим кнопку очистки корзины и кликаем на нее
        clear_cart_button = self.driver.find_element(By.CSS_SELECTOR, ".cart-page__clear-cart-title")
        self.driver.execute_script("arguments[0].click();", clear_cart_button)

    @allure.step("Получить информацию, что корзина очищена")
    def get_information(self):
        # Ожидаем появление элемента с текстом "Корзина очищена"
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-multiple-delete__title")))
        # Получаем текст "Корзина очищена"
        info = self.driver.find_element(
            By.CSS_SELECTOR, ".cart-multiple-delete__title").text
        return info
