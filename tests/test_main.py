import allure
from pages.main_page import MainPage

class TestMainFunctionality:
    @allure.title('Тест перехода в раздел "Лента заказов"')
    def test_follow_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_feed_button()
        assert main_page.check_redirect_to_feed()

    @allure.title('Тест перехода в Конструктор')
    def test_follow_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_feed_button()
        main_page.click_on_builder_button()
        assert main_page.check_redirect_to_main()

    @allure.title('Тест появления окна "Детали ингредиента"')
    def test_show_about_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_red_bun_card()
        assert main_page.wait_ingredient_popup()

    @allure.title('Тест закрытия окна "Детали ингредиента"')
    def test_close_about_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_red_bun_card()
        main_page.wait_ingredient_popup()
        main_page.close_ingredient_popup()
        assert main_page.wait_ingredient_popup_close()

    @allure.title('Тест увеличения счетчика ингредиента при добавлении его в корзину')
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        count_before = int(main_page.get_ingredient_count())
        main_page.add_bun_to_basket()
        count_after = int(main_page.get_ingredient_count())
        assert count_after > count_before