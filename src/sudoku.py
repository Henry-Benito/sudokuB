from menu import Menu
from settings import Settings

class Sudoku:

    def __init__(self):
        self.sudoku_menu = Menu()
        self.sudoku_settings = Settings()
        
if __name__ == '__main__':
    s = Sudoku()