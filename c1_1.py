import time
from constant import OUT_URL
from logic import testcase_list
from utils import reset_page


def c1_1(driver):
    reset_page(driver)

    c1_1 = testcase_list['ExampleTD_SQ1_1']

    # p3. 첫번째 요소 클릭 -> screen_out

    print(f"***{c1_1['current_url']} url check START***")
    driver.find_element_by_id('ExampleTD_SQ1_1').click()
    driver.find_element_by_id("BtnNextPage").click()

    c_url = driver.current_url
    if c_url == OUT_URL:
        print("ExampleTD_SQ1_1  check is OK")
        print(f"***{c1_1['current_url']} url END***")
        print('')
    time.sleep(0.2)
