from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys



def main():
    driver = webdriver.Chrome(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver.exe'))
    driver.set_window_size(1200, 1480)
    driver.get("https://www.olx.ua/")
    search = driver.find_element_by_id('headerSearch')
    search.send_keys('audi')
    search.send_keys(Keys.ENTER)
    driver.find_element_by_tag_name('body').screenshot(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.png'))
    # btn = driver.find_element_by_class_name('cfff x-large margintop-1')
    # btn.click()

    driver.quit()


if __name__ == "__main__":
    main()

