import sys
sys.path.append("..\src")
from settings import Settings
import unittest


class TestSettings(unittest.TestCase):
    def setUp(self):
        pass
    """
def test_settings_should_create_a_new_config_file_if_there_is_not_exists(self):
settings_xml = Settings()
if(not os.path.exists(settings_xml.xml_file_path)):
settings_xml.create_xml_file()
result = os.path.exists(settings_xml.xml_file_path)
self.assertTrue(result)
"""

    def test_set_config_should_update_value_for_algorithm_to_backtracking(self):
        new_default = "Backtracking"
        settings_xml = Settings()
        settings_xml.read_settings_from_file()
        settings_xml.set_config("Algorithm", new_default)
        settings_xml.write_settings()
        settings_xml.read_settings_from_file()
        result = settings_xml.get_name_for_current_setting("Algorithm")
        self.assertEqual(new_default, result)

    def test_set_config_should_update_value_for_level_easy_to_max_35(self):
        setting_node = "Level"
        setting_name = "Easy"
        attribute_name = "max"
        new_attribute_value = "35"
        settings_xml = Settings()
        settings_xml.read_settings_from_file()
        settings_xml.set_config_attributes(setting_node, setting_name, attribute_name, new_attribute_value)
        settings_xml.write_settings()
        settings_xml.read_settings_from_file()
        result = settings_xml.get_attribute_value_for_setting(setting_node, setting_name, attribute_name)
        self.assertEqual(new_attribute_value, result)

    def test_get_current_settings_should_return_current_settings(self):
        settings_xml = Settings()
        settings_xml.read_settings_from_file()
        settings_xml.set_config("Algorithm", "Backtracking")
        settings_xml.set_config("Input", "CSV")
        settings_xml.set_config("Output", "TXT")
        settings_xml.write_settings()
        expected = {"Algorithm":"Backtracking", "Input": "CSV","Output":"TXT", "input_path":"../custom_games", "output_path": "../game_results", "max": "65", "min": "50", "Level": "Hard"}
        current_settings = settings_xml.get_current_settings()
        self.assertEqual(current_settings.keys().sort(), expected.keys().sort())
        self.assertEqual(current_settings.items().sort(), expected.items().sort())



if __name__ == '__main__':
    unittest.main()