from conv_calc.config_data_tests import *
import pytest
from conv_calc.app.application import Application


@pytest.allure.feature('CRUD-тест: выбор валюты')
@pytest.allure.story('Выбор валюты, в которую конвертируем, проверка списка')
@pytest.mark.parametrize(("to_",), [
    ('JPY',),
])
def test_converter(app, to_):
    app.select_converter_to(to_)
    with pytest.allure.step('Выбор валюту в "В"'):
        assert to_ == app.get_select_converter_to(), 'Не удалось выбрать валюту в "В"'



