from selenium import webdriver

from c1_1 import c1_1
from c1_2 import c1_2

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    c1_1(driver)
    c1_2(driver)

    driver.quit()
