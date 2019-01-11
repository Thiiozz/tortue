# coding utf-8

from tortue.main.common.utils.configuration import Configuration


def test_can_load_configuration_from_json_config_file():
    # Given
    c = Configuration("tortue/test/common_test/resources/test_config.json")

    # When
    print(c.config())
    h = c.config()['mongo']['connection_string']

    # Then
    assert 'mongodb://localhost:27017/' == h
