from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from conv_calc.pages.converter import ConverterPage
from selenium.webdriver.common.by import By
import time

class Application(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.converter_page = ConverterPage(driver, base_url)

    def fill_input_form(self, summ):
        time.sleep(1)
        conv_form = self.converter_page.input_summ
        conv_form.clear()
        conv_form.send_keys(summ)
        self.converter_page.is_this_page

    def get_fill_input_form(self):
        return self.converter_page.get_input_value

    def select_converter_from(self, from_):
        self.wait.until(presence_of_element_located((By.XPATH, "//select[@name='converterFrom']/..")))
        self.converter_page.converter_From.click()
        self.driver.find_element_by_xpath("//select[@name='converterFrom']/..//span[contains(text(),"
                                          "" + " '" + from_ + "'" + ")]").click()

    def get_select_converter_from(self):
        return self.driver.find_element_by_xpath("//select[@name='converterFrom']/..//strong").text

    def select_converter_to(self, to_):
        self.wait.until(presence_of_element_located((By.XPATH, "//select[@name='converterTo']/..")))
        self.converter_page.converter_To.click()
        self.driver.find_element_by_xpath("//select[@name='converterTo']/..//span[contains(text(),"
                                          "" + " '" + to_ + "'" + ")]").click()

    def get_select_converter_to(self):
        return self.driver.find_element_by_xpath("//select[@name='converterTo']/..//strong").text

    def select_source(self, source, value):
        self.driver.find_element_by_xpath("//h6[contains(concat(@class,' '),'-title-text') and text()="
                                          "'"+source+"']/../..//div[contains(concat(@class,' '),'-radio__text') "
                                                     "and text()='"+value+"']").click()

    def get_checked_select_source(self, source):
        checked_text = self.driver.find_element_by_xpath("//h6[contains(concat(@class,' '),'-title-text') and text()='"+source+"']/../..//label[contains(concat(@class,' '),'_checked') and @aria-checked='true']//div[@class='kit-radio__text']")
        return checked_text.text

    def press_show_button(self):
        time.sleep(1)
        self.converter_page.show_button.click()
        try:
            self.wait.until(invisibility_of_element_located((By.XPATH, "//span[@class='rates-converter-result__total-to']")))
            return True
        except WebDriverException:
            print('Не удалось нажать кнопку "Показать"')
            return False

    def get_result_conv(self):
        time.sleep(2)
        # self.wait.until(presence_of_element_located((By.XPATH, "//span[@class='rates-converter-result__total-to']")))
        str_ = self.converter_page.get_result_to.text[:-4]
        print(str_)
        if ',' in str_:
            number_ = float(str_.replace(',', '.'))
        else:
            number_ = int(str_)
        return number_
