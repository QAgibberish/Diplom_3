from selenium.webdriver.common.by import By

class MainPageLocators:
    RED_BUN_CARD = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
    RED_BUN_AMOUNT = (By.CSS_SELECTOR, "a[href='/ingredient/61c0c5a71d1f82001bdaaa6d'] .counter_counter__num__3nue1")
    SPICY_SAUCE_CARD = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']")
    MEAT_CARD = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6f']")
    BASKET = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    SAUCES_TAB = (By.XPATH, "//span[contains(text(), 'Соусы')]")
    FILLING_TAB = (By.XPATH, "//span[contains(text(), 'Начинки')]")
    INGREDIENT_POPUP = (By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']/..")
    EXIT_POPUP_BUTTON = (By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']/../button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")
    BUILDER_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    START_COOKING_POPUP = (By.CSS_SELECTOR, "div.Modal_modal__contentBox__sCy8X.pt-30.pb-30")
    ORDER_NUMBER = (By.CSS_SELECTOR, "div.Modal_modal__contentBox__sCy8X.pt-30.pb-30 > h2.Modal_modal__title_shadow__3ikwq")
    EXIT_COOKING_POPUP_BUTTON = (By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']/../button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"