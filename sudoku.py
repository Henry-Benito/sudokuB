from menu import Menu
from settings import Settings

class Sudoku:

    def __init__(self):
        self.sudoku_menu = Menu()
        self.sudoku_settings = Settings()
        self.user_option = self.sudoku_menu.display_main_menu()
        while str(self.user_option) != "-1":
            execute = self.sudoku_menu.menu_option[str(self.user_option)]
            if self.user_option == 3:
                dict_with_new_settings = execute()
                print "Dict:"
                print dict_with_new_settings

                if len(dict_with_new_settings.keys()) <= 2:
                    self.sudoku_settings.set_config(dict_with_new_settings["node_setting"],dict_with_new_settings["new_default_setting"])
                    self.sudoku_settings.write_settings()
                else:
                    if dict_with_new_settings["node_setting"] == "Level":
                        self.sudoku_settings.set_config(dict_with_new_settings["node_setting"],dict_with_new_settings["new_default_setting"])
                        self.sudoku_settings.set_config_attributes(dict_with_new_settings["node_setting"],dict_with_new_settings["new_default_setting"],"min",dict_with_new_settings["new_min"])
                        self.sudoku_settings.set_config_attributes(dict_with_new_settings["node_setting"],dict_with_new_settings["new_default_setting"],"max",dict_with_new_settings["new_max"])
                        self.sudoku_settings.write_settings()
                    elif dict_with_new_settings["node_setting"] == "Output" or dict_with_new_settings["node_setting"] == "Input":
                        self.sudoku_settings.set_config(dict_with_new_settings["node_setting"],dict_with_new_settings["new_default_setting"])
                        aux = dict_with_new_settings["node_setting"].lower()+"_path"
                        self.sudoku_settings.set_config_attributes(dict_with_new_settings["node_setting"],dict_with_new_settings["new_default_setting"],aux,dict_with_new_settings[aux])
                        self.sudoku_settings.write_settings()
                self.user_option = "0"
            else:
			execute()
			self.user_option = self.sudoku_menu.display_submenu()





if __name__ == '__main__':
    s = Sudoku()