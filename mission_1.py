class Game:
    def __init__(self):
        self.theList = [[0, 0, 2], [0, 1, 2], [0, 2, 4], [0, 3, 5]]

    def get_flagged_cells(self):
        list = []
        for x in self.theList:
            if x[2] == 4:
                list.append(x)
        return list

if __name__ == '__main__':
    print(Game().get_flagged_cells())