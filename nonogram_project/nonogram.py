import numpy as np


class Nonogram:
    tiles = np.zeros((0,0))
    size = (1,1)
    x_clues = [[]]
    y_clues = [[]]
    
    #tile_array is an np.array initialized with lists (e.g [[1,0],[0,1]] forming a 2x2 nonogram) 
    def __init__(self, tile_array):
        self.tiles = tile_array
        self.size = tile_array.shape
        self.x_clues = np.zeros((0,0))
        self.y_clues = np.zeros((0,0))
        
    def get_clues(self):
        x_list = []
        y_list = []
        
        for rows in self.tiles:            
            clue_list = []
            clue = 0
            
            #Searches rows to generate the x-clues
            for i in range(len(rows)):
                if rows[i] == 1:
                    clue += 1        
                if i + 1 >= len(rows):
                    if clue == 0:
                        continue
                    else:
                        clue_list.append(clue)
                        continue
                if clue == 0:
                    continue
                if rows[i + 1] == 0:
                    clue_list.append(clue)
                    clue = 0
                    
            x_list.append(clue_list)
        
        #Searches columns to generate the y-clues
        for rows in self.tiles.T:
            clue_list = []
            clue = 0
            for i in range(len(rows)):
                if rows[i] == 1:
                    clue += 1        
                if i + 1 >= len(rows):
                    if clue == 0:
                        continue
                    else:
                        clue_list.append(clue)
                        continue
                if clue == 0:
                    continue
                if rows[i + 1] == 0:
                    clue_list.append(clue)
                    clue = 0
           
            y_list.append(clue_list)
            
        return y_list
                
        
        