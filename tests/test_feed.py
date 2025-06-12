import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage

class TestFeedSection:
    @allure.title('Тест увеличения счетчика "Выполнено за все время"')
    def test_total_count_increase(self, login):
        main_page = MainPage(login)
        feed_page = FeedPage(login)
        main_page.click_on_feed_button()
        count_before = int(feed_page.get_total_count_value())
        main_page.click_on_builder_button()
        main_page.add_bun_to_basket()
        main_page.add_sauce_to_basket()
        main_page.add_filling_to_basket()
        main_page.click_on_order_button()
        main_page.wait_cooking_popup()
        main_page.close_cooking_popup()
        main_page.wait_cooking_popup_close()
        main_page.click_on_feed_button()
        count_after = int(feed_page.get_total_count_value())
        assert count_after > count_before

    @allure.title('Тест увеличения счетчика "Выполнено за сегодня"')
    def test_today_count_increase(self, login):
        main_page = MainPage(login)
        feed_page = FeedPage(login)
        main_page.click_on_feed_button()
        count_before = int(feed_page.get_today_count_value())
        main_page.click_on_builder_button()
        main_page.add_bun_to_basket()
        main_page.add_sauce_to_basket()
        main_page.add_filling_to_basket()
        main_page.click_on_order_button()
        main_page.wait_cooking_popup()
        main_page.close_cooking_popup()
        main_page.wait_cooking_popup_close()
        main_page.click_on_feed_button()
        count_after = int(feed_page.get_today_count_value())
        assert count_after > count_before

    @allure.title('Тест появления номера заказа в разделе "В работе"')
    def test_show_order_number_in_progress(self, login):
        main_page = MainPage(login)
        feed_page = FeedPage(login)
        main_page.add_bun_to_basket()
        main_page.add_sauce_to_basket()
        main_page.add_filling_to_basket()
        main_page.click_on_order_button()
        main_page.wait_cooking_popup()
        order_id = main_page.get_order_id()
        main_page.close_cooking_popup()
        main_page.wait_cooking_popup_close()
        main_page.click_on_feed_button()
        feed_page.wait_for_order_in_progress(order_id)
        in_progress = feed_page.get_in_progress_value()
        assert order_id in in_progress
