from selenium.webdriver.common.by import By

from conv_calc.pages.page import Page


class ConverterPage(Page):

    @property
    def input_summ(self):
        return self.driver.find_element_by_xpath("//input[@placeholder='Сумма']")

    @property
    def get_input_value(self):
        return self.driver.find_element_by_xpath("//input[@placeholder='Сумма']").get_attribute('value')

    @property
    def converter_From(self):
        return self.driver.find_element_by_xpath("//select[@name='converterFrom']/..")

    @property
    def converter_To(self):
        return self.driver.find_element_by_xpath("//select[@name='converterTo']/..")

    @property
    def show_button(self):
        return self.driver.find_element_by_xpath("//button[@class='rates-button' and text()='Показать']")

    @property
    def get_result_to(self):
        return self.driver.find_element_by_xpath("//span[@class='rates-converter-result__total-to']")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.XPATH, "//div[@class='kit-collapse__content']"))
