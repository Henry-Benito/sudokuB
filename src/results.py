class Results:
    def __init__(self):
        pass

    def save_to_file(self, info, saved_route = "../game_results/default"):
        """This function save a solved sudoku puzzle in a TXT file
        Keywords:
        info -- Is a string value that contains a suoku resolved or to resolve e.g. (81.74.... etc)
        saved_route -- is the path were the txt file will be saved
        """
        self.saved_route = saved_route
        self.info = info
        try:
            f = open(self.saved_route+'.txt', 'w')
            f.write(self.info)
            f.close()
            print "A sudoku was written in:" + str(saved_route)
        except:
            raise ("Error writing sudoku in:" + str(saved_route))