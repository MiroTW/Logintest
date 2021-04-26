import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import warnings
import os

class OHF(unittest.TestCase):
    def setUp(self):
#         warnings.simplefilter('ignore', ResourceWarning)
        opts = Options()
#         opts.add_argument("--no-sandbox")
#         opts.add_argument('--headless')
        opts.add_argument('--disable-gpu')
#         opts.add_argument("--no-sandbox")
#         opts.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opts)
        self.driver.get('https://www.104.com.tw/jobs/main/')
#         self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    #login test
    def test(self):
        time.sleep(30)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[2]/ul/li[6]/a').click()
#         self.driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[6]/a').click()
        self.driver.find_element_by_id('username').send_keys(os.environ['USERNAME'])
        self.driver.find_element_by_id('password').send_keys(os.environ['PASSWORD'])
        self.driver.find_element_by_id('submitBtn').click()
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[5]/a').is_displayed()

if __name__ == '__main__':
    unittest.main()
