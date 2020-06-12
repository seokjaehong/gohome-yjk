from selenium import webdriver

from c1_1 import c1_1
from c1_2 import c1_2
from execute_test import execute_test

from utils import get_start_page
from utils.get_logic import get_logic

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    logics = get_logic()

    for logic in logics:
        #1. 시작페이지로 이동
        get_start_page(driver)
        execute_test(driver, logic)

    driver.quit()
