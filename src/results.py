class Results:
    def __init__(self):
        pass

    def save_to_file(self, info, saved_route = "../game_results/default"):
        """This function save a solved sudoku puzzle in a TXT file"""
        self.saved_route = saved_route
        self.info = info
        try:
            f = open(self.saved_route+'.txt', 'w')
            f.write(self.info)
            f.close()
            print "A sudoku was written in:" + str(saved_route)
        except:
            print "Error writing sudoku in:" + str(saved_route)