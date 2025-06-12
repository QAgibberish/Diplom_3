import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data.url import *

class MainPage(BasePage):
    @allure.step('Кликнуть на кнопку "Конструктор"')
    def click_on_builder_button(self):
        self.click_on_element(MainPageLocators.BUILDER_BUTTON)
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Кликнуть на кнопку "Лента Заказов"')
    def click_on_feed_button(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.click_on_element(MainPageLocators.FEED_BUTTON)

    @allure.step('Клик на булку')
    def click_on_red_bun_card(self):
        self.click_on_element(MainPageLocators.RED_BUN_CARD)

    @allure.step('Подождать загрузки всплывающего окна "Детали ингредиента"')
    def wait_ingredient_popup(self):
        return self.wait_for_element(MainPageLocators.INGREDIENT_POPUP).is_displayed()

    @allure.step('Подождать закрытия всплывающего окна "Детали ингредиента"')
    def wait_ingredient_popup_close(self):
        return self.wait_for_element_hide(MainPageLocators.INGREDIENT_POPUP)

    @allure.step('Закрыть окно "Детали ингредиента"')
    def close_ingredient_popup(self):
        self.click_on_element(MainPageLocators.EXIT_POPUP_BUTTON)

    @allure.step('Получить значение счётчика ингредиента')
    def get_ingredient_count(self):
        self.wait_for_element(MainPageLocators.RED_BUN_AMOUNT)
        return self.get_text_on_element(MainPageLocators.RED_BUN_AMOUNT)

    @allure.step('Добавить булку в корзину')
    def add_bun_to_basket(self):
        self.wait_for_element(MainPageLocators.RED_BUN_CARD)
        self.drag_and_drop_element(MainPageLocators.RED_BUN_CARD, MainPageLocators.BASKET)

    @allure.step('Добавить соус в корзину')
    def add_sauce_to_basket(self):
        self.wait_for_element(MainPageLocators.SPICY_SAUCE_CARD)
        self.drag_and_drop_element(MainPageLocators.SPICY_SAUCE_CARD, MainPageLocators.BASKET)

    @allure.step('Добавить начинку в корзину')
    def add_filling_to_basket(self):
        self.wait_for_element(MainPageLocators.MEAT_CARD)
        self.drag_and_drop_element(MainPageLocators.MEAT_CARD, MainPageLocators.BASKET)

    @allure.step('Нажать кнопку "Оформить заказ"')
    def click_on_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Подождать загрузки всплывающего окна "Ваш заказ начали готовить"')
    def wait_cooking_popup(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        return self.wait_for_element(MainPageLocators.START_COOKING_POPUP).is_displayed()

    @allure.step('Получить идентификатор заказа')
    def get_order_id(self):
        return self.get_text_on_element(MainPageLocators.ORDER_NUMBER)

    @allure.step('Подождать закрытия всплывающего окна "Ваш заказ начали готовить"')
    def wait_cooking_popup_close(self):
        return self.wait_for_element_hide(MainPageLocators.START_COOKING_POPUP)

    @allure.step('Закрыть окно "Ваш заказ начали готовить"')
    def close_cooking_popup(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.click_on_element(MainPageLocators.EXIT_COOKING_POPUP_BUTTON)

    @allure.step('Проверить переход на страницу "Лента Заказов"')
    def check_redirect_to_feed(self):
        actual_url = self.wait_and_get_url(feed)
        return actual_url == feed

    @allure.step('Проверить переход на главную страницу')
    def check_redirect_to_main(self):
        actual_url = self.wait_and_get_url(main_site)
        return actual_url == main_site