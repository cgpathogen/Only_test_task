import time

from AnotherPage import Another_page
from conftest import init_driver
from BasePage import BasePage
from MainPage import Main_page


def test_main(init_driver):
    driver = init_driver
    base = BasePage(driver) # создаём экземпляр класса страницы с базовыми методами
    main = Main_page(driver) # создаём экземпляр класса главной страницы
    another = Another_page(driver) # создаём экземпляр класса третьей страницы

    base.go_to_main_url()
    base.click_accept_cookie_btn() # принимаем куки, чтобы gjg-fg не мешал нам видеть, как мы наводим курсор на кнопку в методе hover_start_project_btn :))
    base.scroll_to_footer()
    main.hover_start_project_btn()
    main.print_footer_text()
    main.click_wow_awards_link()
    another.print_title_text()
    another.print_footer_text()
    print("done")