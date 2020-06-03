import time
from constant import OUT_URL
from logic import testcase_list
from utils import get_start_page


def execute_test(driver, logic):
    # get_start_page(driver)
    # len_l = len(logic)
    # cnt = 0

    for i in logic:
        k, v = list(i.keys())[0], list(i.values())[0]
        if k != 'ID':
            driver.find_element_by_id('ExampleTD_{0}_{1}'.format(k, v)).click()
            driver.find_element_by_id("BtnNextPage").click()
            if driver.current_url == OUT_URL:
                # go Back to Start page
                pass

        time.sleep(2)
