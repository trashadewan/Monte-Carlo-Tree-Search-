from enum import Enum

class option(Enum):
    EMPTY = 0
    BEAN = 1
    CORN = 2


class State:

    def __init__(self, farm_size):
        self.farm = [[option.EMPTY.value for i in range(farm_size)] for j in range(farm_size)]
        self.farm_size = farm_size

    def Clone(self):
        """ Create a deep clone of this game state.
        """
        st = State(self.farm_size)
        st.farm = [[self.farm[i][j] for i in range(self.farm_size)] for j in range(self.farm_size)]
        return st

    def DoMove(self, move):
        """ Update a state by carrying out the given move.
            Must update playerJustMoved.
        """
        x, y, plant = move
        if self.farm[x][y] == option.EMPTY.value:
            self.farm[x][y] = plant
            return True
        return False

    def GetMoves(self):
        """ Get all possible moves from this state.
        """
        list_of_moves = list()
        for x in range(self.farm_size):
            for y in range(self.farm_size):
                if self.farm[x][y] == option.EMPTY.value:
                    list_of_moves.append((x, y, option.BEAN.value))
                    list_of_moves.append((x, y, option.CORN.value))
        return list_of_moves

    def convert_move_to_string(self,move):
        x,y,crop = move
        crop1=''
        if crop == option.BEAN.value:
            crop1 = 'bean '
        elif crop == option.CORN.value:
            crop1 = 'corn '
        return "plant "+ crop1+ str(x)+","+str(y)

    def GetResult(self):
        """ Get the game result from the viewpoint of playerjm.
        """
        assert len(self.GetMoves()) == 0
        additional_harvest = 0
        for x in range(self.farm_size):
            for y in range(self.farm_size):
                if self.farm[x][y] == option.CORN.value:
                    if x - 1 >= 0 and y - 1 >= 0 and self.farm[x - 1][y - 1] == option.BEAN.value:
                        additional_harvest += 1
                    if x - 1 >= 0 and self.farm[x - 1][y] == option.BEAN.value:
                        additional_harvest += 1
                    if x - 1 >= 0 and y + 1 < self.farm_size and self.farm[x - 1][y + 1] == option.BEAN.value:
                        additional_harvest += 1
                    if y - 1 >= 0 and self.farm[x][y - 1] == option.BEAN.value:
                        additional_harvest += 1
                    if y + 1 < self.farm_size and self.farm[x][y + 1] == option.BEAN.value:
                        additional_harvest += 1
                    if x + 1 < self.farm_size and y - 1 >= 0 and self.farm[x + 1][y - 1] == option.BEAN.value:
                        additional_harvest += 1
                    if x + 1 < self.farm_size and self.farm[x + 1][y] == option.BEAN.value:
                        additional_harvest += 1
                    if x + 1 < self.farm_size and y + 1 < self.farm_size and self.farm[x + 1][y + 1] == option.BEAN.value:
                        additional_harvest += 1
                    additional_harvest += 10
                if self.farm[x][y] == option.BEAN.value:
                    if x - 1 >= 0 and y - 1 >= 0 and self.farm[x - 1][y - 1] == option.CORN.value:
                        additional_harvest += 15
                        continue
                    if x - 1 >= 0 and self.farm[x - 1][y] == option.CORN.value:
                        additional_harvest += 15
                        continue
                    if x - 1 >= 0 and y + 1 < self.farm_size and self.farm[x - 1][y + 1] == option.CORN.value:
                        additional_harvest += 15
                        continue
                    if y - 1 >= 0 and self.farm[x][y - 1] == option.CORN.value:
                        additional_harvest += 15
                        continue
                    if y + 1 < self.farm_size and self.farm[x][y + 1] == option.CORN.value:
                        additional_harvest += 15
                        continue
                    if x + 1 < self.farm_size and y - 1 >= 0 and self.farm[x + 1][y - 1] == option.CORN.value:
                        additional_harvest += 15
                        continue
                    if x + 1 < self.farm_size and self.farm[x + 1][y] == option.CORN.value:
                        additional_harvest += 15
                        continue
                    if x + 1 < self.farm_size and y + 1 < self.farm_size and self.farm[x + 1][y + 1] == option.CORN.value:
                        additional_harvest += 15
                        continue
                    additional_harvest += 10
        return additional_harvest

    def __repr__(self):
        s = "FarmSize:" + str(self.farm_size)
        return s