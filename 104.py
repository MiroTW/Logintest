import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class OHF(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # cap = DesiredCapabilities().INTERNETEXPLORER
        # cap['nativeEvents'] = False
        # cap['ignoreProtectedModeSettings'] = True
        # cap['disable-popup-blocking'] = True
        # cap['enablePersistentHover'] = True
        # cap['ignoreZoomSetting'] = True
        # self.driver = webdriver.Ie(capabilities=cap)
        self.driver.get('https://www.104.com.tw/jobs/main/')
        self.driver.maximize_window()
        # self.driver.get_screenshot_as_file('D://test_104_home.png')

    def tearDown(self):
        self.driver.quit()

    def Login(self):
        username = 'F127342030'
        password = 'snoopy09'
        self.driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[6]/a').click()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('submitBtn').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[5]/a').is_displayed()
        # self.driver.get_screenshot_as_file('D://test_104_login.png')

    #login test
    def test_01(self):
        self.Login()

    # #logout test
    # def test_02(self):
    #     self.Login()
    #     self.driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[5]/a').click()
    #     self.driver.implicitly_wait(60)
    #     self.driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[6]/a').is_displayed()
    #
    # #personal imformation
    # def test_03(self):
    #     self.Login()
    #     time.sleep(3)
    #     self.driver.find_element_by_id('myName').click()
    #     self.driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[4]/ul/li/div/dl/dt[1]/a').click()
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
    #     time.sleep(3)
    #     self.driver.find_element_by_link_text('下一步').click()
    #     time.sleep(3)
    #     self.driver.find_element_by_link_text('下一步').click()
    #     time.sleep(3)
    #     self.driver.find_element_by_link_text('下一步').click()
    #     time.sleep(3)
    #     self.driver.find_element_by_link_text('我知道了').click()
    #     # time.sleep(3)
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
    #     self.driver.find_element_by_id('myName').click()
    #     self.driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[4]/ul/li/div/dl/dt[1]/a').click()
    #     time.sleep(3)
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
    #     try:
    #         self.driver.find_element_by_link_text('下一步')
    #         next_btn = 'FAIL'
    #     except:
    #         next_btn = 'PASS'
    #     self.assertEqual('PASS', next_btn)
    #     try:
    #         self.driver.find_element_by_id('myName')
    #         print("PASS")
    #     except:
    #         print("FAIL")
    #     self.driver.close()

    #




if __name__ == '__main__':
    unittest.main()