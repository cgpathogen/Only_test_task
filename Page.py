from BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Main_page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, poll_frequency=1, timeout=10)
        self.action = ActionChains(driver)



    # locators

    start_project_btn = ("xpath", "(//button[text()='Начать проект'])[5]")


    # getters

    def get_start_project_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.start_project_btn))


    # actions

    def hover_start_project_btn(self):
        """
        Демонстрационный метод, который наведёт курсор на кнопку, проверяющий наличие кнопки в футере
        """
        self.action.move_to_element(self.driver.find_element(*self.start_project_btn)).pause(3).perform()