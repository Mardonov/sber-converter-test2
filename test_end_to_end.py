from conv_calc.config_data_tests import *
import pytest
from conv_calc.app.application import Application


@pytest.allure.feature('End-to-end сценарий')
@pytest.allure.story('Ввод суммы, выбор некоторых опций, конвертация валюты')
@pytest.mark.parametrize(("summ_", "result", "from_", "to_"), [
    ('1', '1.06', 'GBP', 'EUR'),
])
def test_converter(app, summ_, result, from_, to_):
    app.fill_input_form(summ_)
    with pytest.allure.step('Ввод суммы'):
        assert summ_ == app.get_fill_input_form(), 'Результат не совпадает с ожидаемым'

    app.select_converter_from(from_)
    with pytest.allure.step('Выбор валюту "ИЗ"'):
        assert from_ == app.get_select_converter_from(), 'Не удалось выбрать валюту "ИЗ'

    app.select_converter_to(to_)
    with pytest.allure.step('Выбор валюту "В"'):
        assert to_ == app.get_select_converter_to(), 'Не удалось выбрать валюту "В'

    @pytest.mark.parametrize(
        'source, value', [
            ('Источник', 'Наличные'),
            ('Получение', 'Выдать наличные'),
            ('Способ обмена', 'Отделение (ВСП)'),
            ('Пакет услуг', 'Нет пакета'),
            ('Время', 'Текущее'),
        ]
    )
    def test_select_code(source_, value_):
        app.select_source(source_, value_)
        with pytest.allure.step('Выбор - '+value_+' в блоке - '+source_+''):
            assert value_ == app.get_checked_select_source(source_), 'Не удалось выбрать - '+value_+' в блоке - '+source_+''

    with pytest.allure.step('Вывод результата'):
        assert True == app.press_show_button(), 'Не удалось нажать кнопку "Показать"'

    with pytest.allure.step('Проверка результата'):
        assert float(result) == app.get_result_conv(), 'Результат не совпадает с ожидаемым'


