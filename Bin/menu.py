
import time
from settings import Settings


class Menu:
    def __init__(self):
        self.menu_option = {"m": [self.display_main_menu],
                            "1": [self.start_game],
                            "2": [self.display_settings],
                            "3": [self.display_modify_settings],
                            "3.1": [self.__display_modify_algorithm],
                            "3.1.1": [self.__display_modify_default_setting,
                                      "Algorithm"],
                            "3.2": [self.__display_modify_level],
                            "3.2.1": [self.__display_modify_default_setting, "Level"],
                            "3.2.2": [self.__display_select_setting_name_to_modify_attributes, "Level"],
                            "3.3": [self.__display_modify_input],
                            "3.3.1": [self.__display_modify_default_setting, "Input"],
                            "3.3.2": [self.__display_select_setting_name_to_modify_attributes, "Input"],
                            "3.4": [self.__display_modify_output],
                            "3.4.1": [self.__display_modify_default_setting, "Output"],
                            "3.4.2": [self.__display_select_setting_name_to_modify_attributes, "Output"]}

        self.sudoku_settings = Settings()
        self.status = ""

        while self.status != "exit":
            self.display_main_menu()


    def display_main_menu(self):
        """Display main menu for sudoku game"""
        self.status = "m"
        user_option = str(raw_input("\n\nSUDOKU Menu\n" +
                                    "------------------------\n" +
                                    "1. Play\n" +
                                    "2. Display settings\n" +
                                    "3. Modify settings\n" +
                                    "x. Exit\n" +
                                    "Please enter an option number:"))
        self.__validate_an_option_and_run_it(user_option)

    def start_game(self):
        """Start the game with default settings"""
        print "Trying to start game"

    def display_settings(self):
        """Display configurations values(read from XML config file) for sudoku game"""
        print "\n\nSettings for Sudoku game"
        print "========================"
        list_of_settings = ["Algorithm", "Level", "Input", "Output"]
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
        time.sleep(15)

    EXIT_GAME_OPTION = "x"
    def __validate_an_option_and_run_it(self, user_option):
        """Execute the method according to user_option value

        Keyword arguments:
        user_option -- value of option according to menu
        """
        if user_option is None:
            print "is None"
        if user_option[-1] == self.EXIT_GAME_OPTION:
            self.status = "exit"
        elif user_option[-1] == "m":
            pass
        else:
            list_execute = self.menu_option[user_option]
            function_execute = list_execute[0]
            if len(list_execute) > 1:
                function_execute(list_execute[1])
            else:
                function_execute()

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

        user_option = raw_input("Please enter a number for setting to be modified:")
        self.__validate_an_option_and_run_it(self.status + user_option)

    def __display_modify_algorithm(self):
        """Display menu of different option to modify Algorithm"""

        self.status = "3.1."
        print "\n\nAlgorithm options"
        print "1. Modify algorithm by default"
        print "m. Go to main menu"
        print "x. Exit"

        user_option = raw_input("Please enter a number:")
        self.__validate_an_option_and_run_it(self.status + user_option)

    def __display_modify_level(self):
        """Display menu of different option to modify Level"""

        self.status = "3.2."

        print "\n\nLevel options"
        print "1. Modify level by default"
        print "2. Modify level attributes"
        print "m. Go to main menu"
        print "x. Exit"

        user_option = raw_input("Please enter a number:")
        self.__validate_an_option_and_run_it(self.status + user_option)

    def __display_modify_input(self):
        """Display menu of different option to modify Input"""

        self.status = "3.3."

        print "\n\nInput Games options"
        print "1. Modify Input Game method by default"
        print "2. Modify Input attributes"
        print "m. Go to main menu"
        print "x. Exit"

        user_option = raw_input("Please enter a number:")
        self.__validate_an_option_and_run_it(self.status + user_option)

    def __display_modify_output(self):
        """Display menu of different option to modify Output"""

        self.status = "3.4."

        print "\n\nResults Output options"
        print "1. Modify Result output method by default"
        print "2. Modify Result output attributes"
        print "m. Go to main menu"
        print "x. Exit"

        user_option = raw_input("Please enter a number:")
        self.__validate_an_option_and_run_it(self.status + user_option)

    def __display_modify_default_setting(self, setting_to_modify):
        """Display options for setting to be modifed as the method according to user_option value

        Keyword arguments:
        setting_to_modify -- setting used to get a list of different values
        """
        setting = setting_to_modify
        print "\n\nSet default " + setting
        elements = self.sudoku_settings.get_setting_list_to(setting)
        list_of_settings = []
        counter_index = 1

        for element in elements:
            print str(counter_index)+". " + element.attrib["name"]
            list_of_settings.append(element.attrib["name"])
            counter_index += 1
        print "m. Go to main menu"
        print "x. Exit"

        new_setting = str(raw_input("Please enter a value:"))

        if new_setting == "x":
            self.status = "exit"
        elif new_setting == "m":
            pass
        elif int(new_setting) >= 1 and int(new_setting) <= len(list_of_settings):
            self.sudoku_settings.set_config(setting, list_of_settings[int(new_setting) - 1])
            self.sudoku_settings.write_settings()
        else:
            pass

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
                self.sudoku_settings.set_config_attributes(setting, setting_name, attribute, new_value)
                self.sudoku_settings.write_settings()


if __name__ == '__main__':
    Menu()
