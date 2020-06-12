import time
from constant import OUT_URL
from logic import testcase_list
from utils import get_start_page


def go_previous_page(driver):
    driver.find_element_by_id("BtnPrevPage").click()


def go_next_page(driver):
    driver.find_element_by_id("BtnNextPage").click()


def execute_test(driver, logic):
    # 0. 주관식 입력인경우
    # 1. 객관식인경우
    for i in logic:
        k, v = list(i.keys())[0], list(i.values())[0]
        if k != 'ID':
            if int(v) > 0:
                print(v)
                # typecheck (주관식 입력이 있음)
                if v < 1000:
                    driver.find_element_by_id('ExampleTD_{0}_{1}'.format(k, v)).click()
                elif v >= 1000:
                    a = driver.find_element_by_id('obj{0}'.format(k))
                    a.click()
                    a.send_keys(v)
                go_next_page(driver)
            else:
                if driver.current_url == OUT_URL:
                    print('TEST CHECK ID OK: {0}'.format(logic[0]))
                    go_previous_page(driver)
                    break
                else:
                    print('TEST CHECK ID FAIL: {0}'.format(logic[0]))

        time.sleep(1)
