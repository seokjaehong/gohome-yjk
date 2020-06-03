from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constant import TARGET_HOSTNAME


def get_start_page(driver):
    driver.get(TARGET_HOSTNAME)

    # login 버튼 등장할때까지 대기
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "BtnNextPage")))

    # p1. next 버튼 click
    driver.find_element_by_id("BtnNextPage").click()

    # p2. 다음페이지 click
    driver.find_element_by_id("BtnNextPage").click()
