import time

from conftest import init_driver
from BasePage import BasePage
from Page import Main_page


def test_main(init_driver):
    driver = init_driver
    base = BasePage(driver)
    main = Main_page(driver)
    base.go_to_main_url()
    base.scroll_to_footer()
    time.sleep(3)

    main.hover_start_project_btn()
    base.print_footer_text()
    print("done")