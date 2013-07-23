import re
import time
from settings import Settings


class Menu:
    def __init__(self):

        self.settings = ["Algorithm", "Level", "Input", "Output"]

        self.go_main_menu_option = "m"
        self.exit_game_option = "x"
        self.list_of_char_options = [self.go_main_menu_option, self.exit_game_option]
        self.user_option = ""
        self.sudoku_settings = Settings()
        self.status = ""


    def display_main_menu(self):
        """Display main menu for sudoku game"""
        self.status = ""

        self.menu_string = ("\n\n" +
                            "SUDOKU Menu\n" +
                            "------------------------\n" +
                            "1. Play\n" +
                            "2. Display settings\n" +
                            "3. Modify settings\n" +
                            "4. Generate sudoku game\n" +
                            "x. Exit\n")
        print self.menu_string

    def display_settings(self):
        """Display configurations values(read from XML config file) for sudoku game"""
        print "\n\nSettings for Sudoku game"

        self.menu_string  = "========================\n"
        list_of_settings = self.settings
        for setting in list_of_settings:
            self.menu_string  += "\t" + setting + ":\n"
            elements = self.sudoku_settings.get_setting_list_to(setting)
            for element in elements:
                element_name = "\t\t-" + element.attrib["name"]
                if element.attrib["default"] == "True":
                    element_name += " (Default)"
                self.menu_string  += element_name + "\n"

                attributes = element.attrib.keys()
                for attribute in attributes:
                    if attribute != "name" and attribute != "default":
                        self.menu_string  += "\t\t\t" + attribute + " = " + \
                                             element.attrib[attribute] + "\n"

        self.menu_string  += "========================="
        print self.menu_string
        time.sleep(3)
        self.status = self.go_main_menu_option

    def display_modify_settings(self):
        """Display menu of different settings from XML config file"""

        self.status = "3."
        self.menu_string = "\n\nModifying Settings\n" + \
                           "==================\n" + \
                           "1. Algorithm\n" + \
                           "2. Level\n" + \
                           "3. Input games\n" + \
                           "4. Results\n" + \
                           "m. Back to main menu\n" + \
                           "x. Exit"
        print self.menu_string

    def display_modify_setting_options(self, setting):
        """Display menu of different options to modify a setting"""



        for index_setting in range(1, len(self.settings)+1):
            if self.settings[index_setting - 1] == setting:
                self.status = "3." + str(index_setting) + "."
                index_setting_number = index_setting
                break

        self.menu_string = "\n\nModify " + setting + " options:\n" + \
                           "==========================\n" + \
                           "1. Modify " + setting + " by default\n"

        if index_setting_number != 0: #0 refers to Algorithm
            self.menu_string += "2. Modify " + setting + " attributes\n"

        self.menu_string = self.menu_string + \
                           "m. Go to main menu\n" + \
                           "x. Exit"
        print self.menu_string

    def display_modify_default_setting(self, setting_to_modify):
        """Display options for setting to be modifed as the method according to user_option value

        Keyword arguments:
        setting_to_modify -- setting used to get a list of different values
        """
        self.menu_string = ""
        setting = setting_to_modify
        self.menu_string  += "\n\nSet default " + setting + "\n"
        elements = self.sudoku_settings.get_setting_list_to(setting)
        list_of_settings = []
        good_input_values = ""
        counter_index = 1

        for element in elements:
            self.menu_string += str(counter_index)+". " + element.attrib["name"] + "\n"
            list_of_settings.append(element.attrib["name"])
            good_input_values += "|"+str(counter_index)
            counter_index += 1

        self.menu_string += "m. Go to main menu"  + "\n"
        self.menu_string  += "x. Exit"
        self.get_option_value_from_user("Enter a value to select " + \
                                        setting_to_modify + " by default")

        if self.is_a_valid_option_from_settings(good_input_values) is True:
            self.sudoku_settings.set_config(setting, list_of_settings[int(self.user_option) - 1])
            self.sudoku_settings.write_settings()
        self.status = "m"

    def is_a_valid_option_from_settings(self, good_input_values):
        """Validate a user input value against values that have read from settings
        Keyword arguments:
        good_input_values -- list of different values have read from settings.
        """
        patron_input_values = "^(" + self.exit_game_option + "|" + self.go_main_menu_option + \
                              good_input_values + "){1}$"
        if re.match(good_input_values, self.user_option):
            print self.user_option
            if self.user_option == self.exit_game_option or \
               self.user_option == self.go_main_menu_option:
                return False
            return True
        else:
            return False

    def display_select_setting_name_to_modify_attributes(self, setting_to_modify):
        """Display names of setting to modify his attributes

        Keyword arguments:
        setting_to_modify -- setting used to get a list of different values
        """
        setting = setting_to_modify
        print "\n\nSet attributes for " + setting + ":"
        elements = self.sudoku_settings.get_setting_list_to(setting)
        list_of_settings = []
        counter_index = 1

        for element in elements:
            print str(counter_index)+". " + element.attrib["name"]
            list_of_settings.append(element.attrib["name"])
            counter_index += 1
        print "m. Go to main menu"
        print "x. Exit"
        self.get_option_value_from_user()
        setting_value = self.user_option
        if setting_value == "x":
            self.status = "exit"
        elif int(setting_value) >= 1 and int(setting_value) <= len(list_of_settings):
            self.__set_attributes_for_setting(setting, list_of_settings[int(setting_value) - 1])
        else:
            self.user_option = "m"

    def __set_attributes_for_setting(self, setting, setting_name):
        """Display list of attributes to be modified

        Keyword arguments:
        setting -- name of current setting i.e. Algorithm
        setting_name -- name of setting value i.e. Peter Norvig
        """
        print "\n\nAttributes for " + setting_name + ":"
        elements = self.sudoku_settings.get_setting_list_to(setting)

        for i in range(len(elements)):
            if elements[i].attrib["name"] == setting_name:
                element_index = i
        for attribute in elements[element_index].attrib.keys():
            if attribute != "name" and attribute != "default":
                self.get_option_value_from_user("Please enter a new value for " + attribute + ":")
                new_value = self.user_option
                self.sudoku_settings.set_config_attributes(setting, setting_name, attribute,
                                                           new_value)
                self.sudoku_settings.write_settings()
        self.status = "m"
        print "Settings changed successfully.\nReturning to main menu..."

    def exit(self):
        """
        Update status value in order to exit the game.
        """
        self.status = self.exit_game_option

    def go_to_main_menu(self):
        """
        Update status value in order to go to main menu
        """
        self.status = self.go_main_menu_option

    def get_option_value_from_user(self, message = "Please enter an option:"):
        """Get and update the value for user_option from user input"""
        try:
            self.user_option = str(raw_input(message))
        except:
            print "Wrong input value.Returning to main menu"
            self.user_option = "m"

