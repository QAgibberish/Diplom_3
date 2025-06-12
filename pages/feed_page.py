import allure
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage

class FeedPage(BasePage):
    @allure.step('Получить значение счетчика "Выполнено за все время"')
    def get_total_count_value(self):
        self.wait_for_element(FeedPageLocators.TOTAL_COUNT)
        return self.get_text_on_element(FeedPageLocators.TOTAL_COUNT)

    @allure.step('Получить значение счетчика "Выполнено за сегодня"')
    def get_today_count_value(self):
        self.wait_for_element(FeedPageLocators.TODAY_COUNT)
        return self.get_text_on_element(FeedPageLocators.TODAY_COUNT)

    @allure.step('Ожидание появления номера заказа в разделе "В работе"')
    def wait_for_order_in_progress(self, order_id):
        self.wait_for_text_in_element(FeedPageLocators.ORDERS_IN_PROGRESS, order_id)

    @allure.step('Получить содержимое раздела "В работе"')
    def get_in_progress_value(self):
        self.wait_for_element(FeedPageLocators.ORDERS_IN_PROGRESS, timeout=40)
        return self.get_text_on_element(FeedPageLocators.ORDERS_IN_PROGRESS)
