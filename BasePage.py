from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, poll_frequency=1, timeout=10)
        self.action = ActionChains(driver)


    base_url = "https://only.digital/"

    # locators

    footer_xpath = ("xpath","//footer[@class='Footer_root___6Q28']")
    footer_text = ("xpath","//p[@class='text2 Footer_text___ATim']")
    accept_cookie_btn = ("xpath", "/html/body/div[2]/button")

    # getters


    def get_footer(self):
        return self.wait.until(EC.presence_of_element_located(self.footer_xpath))


    def get_footer_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.footer_text))


    def get_cookie_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.accept_cookie_btn))


    # actions


    def click_accept_cookie_btn(self):
        self.get_cookie_button().click()
        print("Приняты куки")


    def go_to_main_url(self):
        self.driver.get(url=self.base_url)


    def print_footer_text(self):
        """
        Выведем на печать url страницы и текст одного из элементов страницы, который содержится в футере
        """
        print(f"\nТекст из подвала страницы {self.driver.current_url} - {self.get_footer_text().text}")


    def scroll_to_footer(self):
        """
        скролл до футера страницы с использованием JS
        """
        footer = self.get_footer()
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'end'});", footer)
        print(f"скролл до футера на странице {self.driver.current_url}")