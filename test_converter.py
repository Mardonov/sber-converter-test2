from conv_calc.config_data_tests import *
import pytest
from conv_calc.app.application import Application


@pytest.allure.feature('Калькулятор иностранных валют. CRUD-тест: поле ввода суммы')
@pytest.allure.story('Ввод различных параметров и проверка результата')
@pytest.mark.parametrize(("summ_", "result"), [
    ('1', '0.02'),
])
def test_converter(app, summ_, result):
    app.fill_input_form(summ_)
    with pytest.allure.step('Ввод суммы'):
        assert summ_ == app.get_fill_input_form(), 'Результат не совпадает с ожидаемым'

    with pytest.allure.step('Вывод результата'):
        assert True == app.press_show_button(), 'Не удалось нажать кнопку "Показать"'

    with pytest.allure.step('Проверка результата'):
        assert float(result) == app.get_result_conv()
