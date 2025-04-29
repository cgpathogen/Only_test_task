from BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Another_page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, poll_frequency=1, timeout=10)
        self.action = ActionChains(driver)


    # locators

    title = ("xpath","/html/body/main/section[6]/div[1]/div/h4")


    # getters

    def get_title(self):
        """
        получаем заголовок со страницы наград
        """
        return self.wait.until(EC.presence_of_element_located(self.title))


    # actions


    def print_title_text(self):
        print(f"Текст заголовка страницы {self.driver.current_url} - {self.get_title().text}")