from constant import OUT_URL
from logic import testcase_list
from utils import get_start_page
import time

sec=0.4

def c1_2(driver):
    get_start_page(driver)
    time.sleep(sec)
    c1_2 = testcase_list['ExampleTD_SQ1_2']

    # p3. 첫번째 요소 클릭 -> screen_out
    driver.find_element_by_id('ExampleTD_SQ1_2').click()
    time.sleep(sec)
    driver.find_element_by_id("BtnNextPage").click()
    time.sleep(sec)
    if driver.current_url == c1_2['current_url']:
        print(f"***{c1_2['current_url']} url check START***")

    # SQ2 page start
    driver.find_element_by_id('ExampleTD_SQ2_1').click()
    time.sleep(sec)
    driver.find_element_by_id("BtnNextPage").click()
    time.sleep(sec)
    if driver.current_url == OUT_URL:
        print("ExampleTD_SQ2_1 check is OK")
        driver.find_element_by_id("BtnPrevPage").click()
    time.sleep(sec)

    driver.find_element_by_id('ExampleTD_SQ2_2').click()
    time.sleep(sec)
    driver.find_element_by_id("BtnNextPage").click()
    time.sleep(sec)
    if driver.current_url == OUT_URL:
        print("ExampleTD_SQ2_2 check is OK")
        driver.find_element_by_id("BtnPrevPage").click()
    time.sleep(sec)

    driver.find_element_by_id('ExampleTD_SQ2_3').click()
    time.sleep(sec)
    driver.find_element_by_id("BtnNextPage").click()
    time.sleep(sec)
    if driver.current_url == OUT_URL:
        print("ExampleTD_SQ2_3 check is OK")
        driver.find_element_by_id("BtnPrevPage").click()
    time.sleep(sec)

    driver.find_element_by_id('ExampleTD_SQ2_4').click()
    time.sleep(sec)
    driver.find_element_by_id("BtnNextPage").click()
    time.sleep(sec)
    if driver.current_url == OUT_URL:
        print("ExampleTD_SQ2_4 check is OK")
        driver.find_element_by_id("BtnPrevPage").click()
    time.sleep(sec)

    driver.find_element_by_id('ExampleTD_SQ2_5').click()
    time.sleep(sec)
    driver.find_element_by_id("BtnNextPage").click()
    time.sleep(sec)
    if driver.current_url == OUT_URL:
        print("ExampleTD_SQ2_5 check is OK")
        driver.find_element_by_id("BtnPrevPage").click()
    time.sleep(sec)

    driver.find_element_by_id('ExampleTD_SQ2_6').click()
    time.sleep(sec)
    driver.find_element_by_id("BtnNextPage").click()
    time.sleep(sec)
    if driver.current_url == "http://svy.web-survey.co.kr/sp2/S11430vprxsa/svyJ005.asp":
        print(f"***{c1_2['current_url']} check END***")
    time.sleep(sec)