import xml.etree.ElementTree as ET


class Settings:

    def __init__(self):
        self.root = ET.Element('sudoku')
        self.xml_file_path = "../src/config.xml"
        self.read_settings_from_file()

    def get_setting_list_to(self, setting):
        """Return a list of elements according to setting value as input parameter"""
        list_of_elements = self.root.findall(".//" + setting)
        return list_of_elements

    def get_current_settings(self):
        """This method gets current settings.
        It returns a dictionary with current default settings"""
        self.read_settings_from_file()
        current_settings = {}
        elements = self.root.findall('.//*[@default="True"]')
        for element in elements:
            if str(element.tag) == "Level":
                current_settings["max"] = element.attrib["max"]
                current_settings["min"] = element.attrib["min"]
            elif str(element.tag) == "Input":
                current_settings["input_path"] = element.attrib["path"]
            elif str(element.tag) == "Output":
                current_settings["output_path"] = element.attrib["path"]
            current_settings[str(element.tag)] = element.attrib["name"]
        return current_settings

    def get_name_for_current_setting(self, setting):
        """This method returns the name for current setting. In other words the
        setting with default value equals True
        Keyword arguments:
        setting -- name of the setting as string(default None)"""
        for element in self.root.iter(setting):
            if element.attrib["default"] == 'True':
                return element.attrib["name"]
        return "None Element"

    def get_attribute_value_for_setting(self, node_setting, setting_name, attribute):
        """This method returns the name for current setting. In other words the
        setting with default value equals True
        Keyword arguments:
        setting -- name of the setting as string(default None)"""
        for element in self.root.iter(node_setting):
            if element.attrib["name"] == setting_name:
                return element.attrib[attribute]
        return "None Element"

    def set_config(self, node_setting, new_default_setting):
        """This method updates the 'default' value to 'True' for the setting.
        Keyword arguments:
        node_setting -- name of the node to find settings. String(default None)
        new_default_setting -- new setting to be default setting.
        String(default None)"""
        for element in self.root.iter(node_setting):
            if element.attrib["name"] == new_default_setting:
                element.set('default', 'True')
            else:
                element.attrib["default"] = 'False'

    def set_config_attributes(self, node_setting, setting_name, attribute, new_value):
        """This method updates the 'default' value to 'True' for the setting.
        Keyword arguments:
        setting -- name of the setting as string(default None)
        setting_name -- name of the setting as string(default None)
        new_value -- new value of the setting as string(default None)
        attribute -- name of attribute in the setting to update his value as string(default None)"""
        for element in self.root.iter(node_setting):
            if element.attrib["name"] == setting_name:
                element.set(attribute, new_value)

    def write_settings(self):
        """Write configuration to XML config file"""
        self.tree = ET.ElementTree(self.root)
        self.tree.write(self.xml_file_path)

    def read_settings_from_file(self):
        """This method update the 'tree' and 'root' data parsed
        from XML config file"""
        self.tree = ET.parse(self.xml_file_path)
        self.root = self.tree.getroot()
