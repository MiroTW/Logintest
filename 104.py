import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class OHF(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome()
        opts = Options()
        opts.add_argument('--headless')
        opts.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opts)
        self.driver.get('https://www.104.com.tw/jobs/main/')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    #login test
    def test(self):
        self.driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[6]/a').click()
        self.driver.find_element_by_id('username').send_keys(USERNAME)
        self.driver.find_element_by_id('password').send_keys(PASSWORD)
        self.driver.find_element_by_id('submitBtn').click()
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[5]/a').is_displayed()

if __name__ == '__main__':
    unittest.main()
