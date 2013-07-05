"""
<SUDOKU>

    <Algorithms>
        <Algorithm default="False" name="Peter Norvig" />
        <Algorithm default="True" name="Backtracking" />
        <Algorithm default="False" name="Brute Force" />
    </Algorithms>

    <Levels>
        <Level default="True" max="25" min="20" name="Easy" />
        <Level default="False" max="35" min="30" name="Medium" />
        <Level default="False" max="45" min="40" name="Hard" />
    </Levels>

    <Outputs>
        <Output default="True" name="Console" />
        <Output default="False" name="Text File" />
        <Output default="False" name="CSV file" />
    </Outputs>

    <Inputs>
        <Input default="False" name="Console" />
        <Input default="True" name="Text File" />
        <Input default="False" name="CSV File" />
    </Inputs>

</SUDOKU>
"""
import xml.etree.ElementTree as ET


class Settings:

    def __init__(self):
        self.root = ET.Element('sudoku')
        self.xml_file_path = "Config.xml"
        self.read_settings_from_file()

    def get_setting_list_to(self, setting):
        list_of_elements = self.root.findall(".//" + setting)
        return list_of_elements

    def get_current_settings(self):
        """This method gets current settings. It returns a list of elements"""
        elements = self.root.findall(".//[@default='True']")
        return elements

    def get_name_for_current_setting(self, setting):
        """This method returns the name for current setting. In other words the
        setting with default value equals True

        Keyword arguments:
        setting -- name of the setting as string(default None)
        """
        for element in self.root.iter(setting):
            if element.attrib["default"] == 'True':
                return element.attrib["name"]
        return "None Element"

    def get_attribute_value_for_setting(self, node_setting, setting_name, attribute):
        """This method returns the name for current setting. In other words the
        setting with default value equals True

        Keyword arguments:
        setting -- name of the setting as string(default None)
        """
        for element in self.root.iter(node_setting):
            if element.attrib["name"] == setting_name:
                return element.attrib[attribute]
        return "None Element"

    def set_config(self, node_setting, new_default_setting):
        """This method updates the 'default' value to 'True' for the setting.

        Keyword arguments:
        node_setting -- name of the node to find settings. String(default None)
        new_default_setting -- new setting to be default setting. String(default None)
        """
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
        attribute -- name of attribute in the setting to update his value as string(default None)
        """
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
