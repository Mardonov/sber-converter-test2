from conv_calc.config_data_tests import *
import pytest
from conv_calc.app.application import Application


@pytest.allure.feature('CRUD-тест: выбор валюты')
@pytest.allure.story('Выбор валюты, из которой конвертируем, проверка списка')
@pytest.mark.parametrize(("from_",), [
        ('GBP',),
])
def test_converter(app, from_):
    app.select_converter_from(from_)
    with pytest.allure.step('Выбор валюту "ИЗ"'):
        assert from_ == app.get_select_converter_from(), 'Не удалось выбрать валюту "ИЗ"'



