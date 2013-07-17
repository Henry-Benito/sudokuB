import re
import time
from settings import Settings


class Menu:
    def __init__(self):

        self.settings = ["Algorithm", "Level", "Input", "Output"]

        self.go_main_menu_option = "m"
        self.exit_game_option = "x"
        self.list_of_char_options = [self.go_main_menu_option, self.exit_game_option]
        self.menu_options = {self.exit_game_option: [self.exit],
                             self.go_main_menu_option: [self.go_to_main_menu],
                             "1": [self.start_game],
                             "2": [self.display_settings],
                             "3": [self.display_modify_settings],
                             "3.1": [self.display_modify_setting_options, self.settings[0]],
                             "3.1.1": [self.__display_modify_default_setting,
                                       self.settings[0]],
                             "3.2": [self.display_modify_setting_options, self.settings[1]],
                             "3.2.1": [self.__display_modify_default_setting, self.settings[1]],
                             "3.2.2": [self.__display_select_setting_name_to_modify_attributes,
                                       self.settings[1]],
                             "3.3": [self.display_modify_setting_options, self.settings[2]],
                             "3.3.1": [self.__display_modify_default_setting, self.settings[2]],
                             "3.3.2": [self.__display_select_setting_name_to_modify_attributes,
                                       self.settings[2]],
                             "3.4": [self.display_modify_setting_options, self.settings[3]],
                             "3.4.1": [self.__display_modify_default_setting, self.settings[3]],
                             "3.4.2": [self.__display_select_setting_name_to_modify_attributes,
                                       self.settings[3]]}

        self.sudoku_settings = Settings()
        self.status = ""

    def run_application(self):
        """Run """
        while self.status != self.exit_game_option:
            if self.status == self.go_main_menu_option or self.status == "":
                self.display_main_menu()
            self.get_option_value_from_user()
            self.validate_user_option()
            self.__run_method_according_option()

    def get_option_value_from_user(self):
        """Get and update the value for user_option from user input"""
        try:
            self.user_option = str(raw_input("Please enter an option:"))
        except:
            self.user_option = "m"

    def validate_user_option(self):
        """Validate input from user and return None if it is a non valid key
        """
        good_input_values = "^(" + self.exit_game_option + "|" + self.go_main_menu_option \
                            + "|\d){1}$"
        if re.match(good_input_values, self.user_option):
            self.user_option = self.status + self.user_option
            last_character = self.user_option[-1]
            if self.__is_a_char_option(last_character) is True:
                self.user_option = last_character
            if not self.menu_options.has_key(self.user_option):
                self.user_option = None
        else:
            self.user_option = "m"

    def __is_a_char_option(self, last_character):
        """Return True if the character belongs to list_of_char_options

        Keyword arguments:
        last_character -- a character value i.e.: x
        """
        for char_options in self.list_of_char_options:
            if self.menu_options.has_key(last_character) and char_options == last_character:
                return True
        return False

    def __run_method_according_option(self):
        """Execute the method according to user_option value

        Keyword arguments:
        user_option -- value of option according to menu
        """
        if self.user_option is not None:
            list_execute = self.menu_options[self.user_option]
            function_execute = list_execute[0]
            if len(list_execute) > 1:
                function_execute(list_execute[1])
            else:
                function_execute()
        else:
            self.status = self.go_main_menu_option

    def display_main_menu(self):
        """Display main menu for sudoku game"""
        self.status = ""
        print ("\n\n" +
               "SUDOKU Menu\n" +
               "------------------------\n" +
               "1. Play\n" +
               "2. Display settings\n" +
               "3. Modify settings\n" +
               "x. Exit\n")

    def start_game(self):
        """Start the game with default settings"""
        print "\n\nTrying to start game.....\n\n"
        self.status = self.go_main_menu_option

    def display_settings(self):
        """Display configurations values(read from XML config file) for sudoku game"""
        print "\n\nSettings for Sudoku game"
        print "========================"
        list_of_settings = self.settings
        for setting in list_of_settings:
            print "\t", setting, ":"
            elements = self.sudoku_settings.get_setting_list_to(setting)
            for element in elements:
                element_name = "\t\t-" + element.attrib["name"]
                if element.attrib["default"] == "True":
                    element_name += " (Default)"
                print element_name

                attributes = element.attrib.keys()
                for attribute in attributes:
                    if attribute != "name" and attribute != "default":
                        print "\t\t\t" + attribute + " = " + element.attrib[attribute]

        print "========================="
        time.sleep(3)
        self.status = self.go_main_menu_option

    def display_modify_settings(self):
        """Display menu of different settings from XML config file"""

        self.status = "3."

        print "\n\nModifying Settings"
        print "=================="
        print "1. Algorithm"
        print "2. Level"
        print "3. Input games"
        print "4. Results"
        print "m. Back to main menu"
        print "x. Exit"

    def display_modify_setting_options(self, setting):
        """Display menu of different options to modify a setting"""

        self.menu_string = ""

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

    def __display_modify_default_setting(self, setting_to_modify):
        """Display options for setting to be modifed as the method according to user_option value

        Keyword arguments:
        setting_to_modify -- setting used to get a list of different values
        """
        setting = setting_to_modify
        print "\n\nSet default " + setting
        elements = self.sudoku_settings.get_setting_list_to(setting)
        list_of_settings = []
        good_input_values = ""
        counter_index = 1

        for element in elements:
            print str(counter_index)+". " + element.attrib["name"]
            list_of_settings.append(element.attrib["name"])
            good_input_values += "|"+str(counter_index)
            counter_index += 1

        print "m. Go to main menu"
        print "x. Exit"
        self.get_option_value_from_user()

        if self.is_a_valid_option_from_settings(good_input_values):
            self.sudoku_settings.set_config(setting, list_of_settings[int(self.user_option) - 1])
            self.sudoku_settings.write_settings()
        self.status = "m"

    def is_a_valid_option_from_settings(self, good_input_values):
        """Validate a user input value against values that have read from settings
        Keyword arguments:
        good_input_values -- list of different values have read from settings.
        """
        print good_input_values
        patron_input_values = "^(" + self.exit_game_option + "|" + self.go_main_menu_option + \
                              good_input_values + "){1}$"
        print patron_input_values
        if re.match(good_input_values, self.user_option):
            print self.user_option
            if self.user_option == self.exit_game_option or \
               self.user_option == self.go_main_menu_option:
                return False
            return True
        else:
            return False

    def __display_select_setting_name_to_modify_attributes(self, setting_to_modify):
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

        setting_value = str(raw_input("Please enter a value:"))

        if setting_value == "x":
            self.status = "exit"
        elif setting_value == "m":
            pass
        elif int(setting_value) >= 1 and int(setting_value) <= len(list_of_settings):
            self.__set_attributes_for_setting(setting, list_of_settings[int(setting_value) - 1])
        else:
            pass

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
                new_value = str(raw_input("Please enter a new value for " + attribute + ":"))
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

    def get_sudoku_from_console(self):
        """
        Return a string from user that contains a sudoku to solve.
        """
        sudoku_from_console = ""
        for row in range(9):
            try:
                console_row = str(raw_input("Enter the 9 digits for %s row of sudoku:" % str(row)))
                sudoku_from_console += console_row
            except:
                sudoku_from_console = None
        return sudoku_from_console

    def inbound_sudoku_has_good_format(self, inbound_sudoku):
        """
        Return True when the string only contains numbers from 0 to 9 or '.' character and
        its length is 81.

        Keyword arguments:
        inbound_sudoku -- string with values for sudoku game from user i.e.:
        400000805030000000000700000020000060000080400000010000
        """
        if re.match("^(\.|[0-9])+$", inbound_sudoku) and len(inbound_sudoku) == 81:
            return True
        else:
            return False

if __name__ == '__main__':
    m = Menu()
    m.run_application()
