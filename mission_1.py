# Clean code: Avoid missinformation
# Refactoring: Extract variable / extract constant
# Refactoring: Rename variable
# Tell-don't-ask 

STATUS = 2
FLAGGED_CELLS = 4

class Cell:
    def __init__(self, position_x, position_y, status):
        self.position_x = position_x
        self.position_y = position_y
        self.status = status
    
    def is_flagged(self):
        return self.status == FLAGGED_CELLS

    def to_list(self):
        return [self.position_x, self.position_y, self.status]

class Game:

    def __init__(self):
        self.board = [Cell(0, 0, 2), Cell(0, 1, 2), Cell(0, 2, 4), Cell(0, 3, 5)]

    def get_flagged_cells(self):
        flagged_cells = []
        for cell in self.board:
            if cell.is_flagged():
                flagged_cells.append(cell.to_list())
        return flagged_cells

if __name__ == '__main__':
    print(Game().get_flagged_cells())