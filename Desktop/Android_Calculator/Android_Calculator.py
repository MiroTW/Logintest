import unittest
import HTMLTestRunner
from appium import webdriver

class TestCalculator(unittest.TestCase):

    def setUp(self):
        print('Setup')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = '.Calculator'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        print('Teardown')
        self.driver.quit()

    def button(self, btn):
        # sleep(5)
        return 'com.android.calculator2:id/'+str(btn)

    def check(self, value):
        # sleep(5)
        return 'com.android.calculator2:id/'+str(value)

    #test number 0
    def test_num_0(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.assertEqual('0', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 1
    def test_num_1(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.assertEqual('1', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 2
    def test_num_2(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.assertEqual('2', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 3
    def test_num_3(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.assertEqual('3', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 4
    def test_num_4(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_4').click()
        self.assertEqual('4', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 5
    def test_num_5(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
        self.assertEqual('5', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 6
    def test_num_6(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_6').click()
        self.assertEqual('6', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 7
    def test_num_7(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_7').click()
        self.assertEqual('7', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 8
    def test_num_8(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
        self.assertEqual('8', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 9
    def test_num_9(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_9').click()
        self.assertEqual('9', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test dec_point
    def test_dec_point(self):
        self.driver.find_element_by_id('com.android.calculator2:id/dec_point').click()
        self.assertEqual('.', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test equal
    def test_equal(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        self.assertEqual('0', self.driver.find_element_by_id('com.android.calculator2:id/result').text)

    #test result text
    def test_result_text(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.assertEqual('3×3', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('9', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        self.assertEqual('9', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.assertEqual('9×', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        self.assertEqual('9', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/dec_point').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        self.assertEqual('.', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('Bad expression', self.driver.find_element_by_id('com.android.calculator2:id/result').text)

    #test delete
    def test_delete(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_4').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_6').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_7').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
        self.assertEqual('3345678', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.assertEqual('3345', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.assertEqual('3345+', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.assertEqual('3345', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test add
    def test_func_add(self):
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.assertEqual('', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.assertEqual('1+2', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('3', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.assertEqual('1+2+3', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('6', self.driver.find_element_by_id('com.android.calculator2:id/result').text)

    #test sub
    def test_func_sub(self):
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.assertEqual('−', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.assertEqual('−1−2', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('−3', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_6').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.assertEqual('−1−2+6−2', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('1', self.driver.find_element_by_id('com.android.calculator2:id/result').text)

    #test mul
    def test_func_mul(self):
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.assertEqual('', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.assertEqual('1×2', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('2', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_6').click()
        self.assertEqual('1×2×6', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('12', self.driver.find_element_by_id('com.android.calculator2:id/result').text)

    #test div
    def test_func_div(self):
        self.driver.find_element_by_id('com.android.calculator2:id/op_div').click()
        self.assertEqual('', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_div').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.assertEqual('1÷2', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('0.5', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/op_div').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
        self.assertEqual('1÷2÷5', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('0.1', self.driver.find_element_by_id('com.android.calculator2:id/result').text)

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestCalculator("test_num_0"))
    suit.addTest(TestCalculator("test_num_1"))
    suit.addTest(TestCalculator("test_num_2"))
    suit.addTest(TestCalculator("test_num_3"))
    suit.addTest(TestCalculator("test_num_4"))
    suit.addTest(TestCalculator("test_num_5"))
    suit.addTest(TestCalculator("test_num_6"))
    suit.addTest(TestCalculator("test_num_7"))
    suit.addTest(TestCalculator("test_num_8"))
    suit.addTest(TestCalculator("test_num_9"))
    suit.addTest(TestCalculator("test_dec_point"))
    suit.addTest(TestCalculator("test_equal"))
    suit.addTest(TestCalculator("test_result_text"))
    suit.addTest(TestCalculator("test_delete"))
    suit.addTest(TestCalculator("test_func_add"))
    suit.addTest(TestCalculator("test_func_sub"))
    suit.addTest(TestCalculator("test_func_mul"))
    suit.addTest(TestCalculator("test_func_div"))

    fp = open('C:/Users/Miro/Desktop/result.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='Android Calculator Test Report',
            description='Android Calculator Test'
        )
    runner.run(suit)