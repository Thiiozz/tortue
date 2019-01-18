# coding utf-8

from tortue.main.common.utils.configuration import Configuration


def test_can_load_configuration_from_json_config_file():
    # Given
    Configuration.instance().load_from_file("tortue/test/common_test/resources/test_config.json")

    # When
    h = Configuration.instance().config()['mongo']['connection_string']

    # Then
    assert 'mongodb://test-host:27017/' == h
