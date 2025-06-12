from selenium.webdriver.common.by import By

class FeedPageLocators:
    TOTAL_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/../p[contains(@class, 'OrderFeed_number')]")
    TODAY_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/../p[contains(@class, 'OrderFeed_number')]")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li")