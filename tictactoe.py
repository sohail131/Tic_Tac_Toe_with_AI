import random


# write your code here
class TicTacToe:
    def __init__(self):
        self.game_table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.coordinates = [[(0, 2), (1, 2), (2, 2)], [(0, 1), (1, 1), (2, 1)], [(0, 0), (1, 0), (2, 0)]]
        self.count = 0
        self.difficulty_levels = ("easy", "medium", "hard")
        self.move = ""

    def game_function(self):
        outer = True

        while outer:
            input_list = input("Input command: ").split()

            if input_list[0] == "exit":
                outer = False
            elif len(input_list) < 3:
                print("Bad parameters!")
            elif input_list[0] == "start":
                self.show_table()
                inner = True
                if "easy" in input_list:
                    self.mode = "easy"
                elif "medium" in input_list:
                    self.mode = "medium"
                elif "hard" in input_list:
                    self.mode = "hard"
                while inner:
                    if (input_list[1] in self.difficulty_levels) and (input_list[2] in self.difficulty_levels):
                        if self.computer_play():
                            self.game_table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                            inner = False
                        elif self.computer_play():
                            self.game_table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                            inner = False
                    elif (input_list[1] in self.difficulty_levels) and (input_list[2] == "user"):
                        if self.computer_play():
                            self.game_table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                            inner = False
                        elif self.user_play():
                            self.game_table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                            inner = False
                    elif (input_list[1] == "user") and (input_list[2] in self.difficulty_levels):
                        if self.user_play():
                            self.game_table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                            inner = False
                        elif self.computer_play():
                            self.game_table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                            inner = False
                    elif (input_list[1] == "user") and (input_list[2] == "user"):
                        if self.user_play():
                            self.game_table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                            inner = False
                        elif self.user_play():
                            self.game_table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                            inner = False

    def user_play(self):
        while True:
            try:
                print("Enter the coordinates: ", end="")
                entered_coordinates = input().split()
                x, y = int(entered_coordinates[0]), int(entered_coordinates[1])

                if (x in range(1, 4)) and (y in range(1, 4)):
                    k = (x - 1, y - 1)
                    new_coordinates = next(((i, j.index(k)) for i, j in enumerate(self.coordinates) if k in j), None)
                    if ((self.game_table[new_coordinates[0]][new_coordinates[1]] == " ") or
                            (self.game_table[new_coordinates[0]][new_coordinates[1]] == "_")):
                        if self.count % 2 == 0:
                            self.game_table[new_coordinates[0]][new_coordinates[1]] = "X"
                        else:
                            self.game_table[new_coordinates[0]][new_coordinates[1]] = "O"
                        self.count += 1
                        self.show_table()
                        status = self.check_game_status()
                        if status in ("X wins", "O wins", "Draw"):
                            print(status)
                            self.count = 0
                            return True
                        else:
                            return False
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("Coordinates should be from 1 to 3!")
            except BaseException:
                print("You should enter numbers!")

    def computer_play(self):
        print(f"Making move level \"{self.mode}\"")

        while True:
            x, y = random.randint(1, 3), random.randint(1, 3)
            k = (x - 1, y - 1)
            new_coordinates = next(((i, j.index(k)) for i, j in enumerate(self.coordinates) if k in j), None)
            if ((self.game_table[new_coordinates[0]][new_coordinates[1]] == " ") or
                    (self.game_table[new_coordinates[0]][new_coordinates[1]] == "_")):
                if self.count % 2 == 0:
                    self.game_table[new_coordinates[0]][new_coordinates[1]] = "X"
                else:
                    self.game_table[new_coordinates[0]][new_coordinates[1]] = "O"
                self.count += 1
                self.show_table()
                status = self.check_game_status()
                if status in ("X wins", "O wins", "Draw"):
                    print(status)
                    self.count = 0
                    return True
                else:
                    return False

    def check_game_status(self):
        if (self.game_table[0][0] == self.game_table[0][1] == self.game_table[0][2] == "X") or (
                self.game_table[1][0] == self.game_table[1][1] == self.game_table[1][2] == "X") or (
                self.game_table[2][0] == self.game_table[2][1] == self.game_table[2][2] == "X") or (
                self.game_table[0][0] == self.game_table[1][0] == self.game_table[2][0] == "X") or (
                self.game_table[0][1] == self.game_table[1][1] == self.game_table[2][1] == "X") or (
                self.game_table[0][2] == self.game_table[1][2] == self.game_table[2][2] == "X") or (
                self.game_table[0][0] == self.game_table[1][1] == self.game_table[2][2] == "X") or (
                self.game_table[0][2] == self.game_table[1][1] == self.game_table[2][0] == "X"):
            return "X wins"
        elif (self.game_table[0][0] == self.game_table[0][1] == self.game_table[0][2] == "O") or (
                self.game_table[1][0] == self.game_table[1][1] == self.game_table[1][2] == "O") or (
                self.game_table[2][0] == self.game_table[2][1] == self.game_table[2][2] == "O") or (
                self.game_table[0][0] == self.game_table[1][0] == self.game_table[2][0] == "O") or (
                self.game_table[0][1] == self.game_table[1][1] == self.game_table[2][1] == "O") or (
                self.game_table[0][2] == self.game_table[1][2] == self.game_table[2][2] == "O") or (
                self.game_table[0][0] == self.game_table[1][1] == self.game_table[2][2] == "O") or (
                self.game_table[0][2] == self.game_table[1][1] == self.game_table[2][0] == "O"):
            return "O wins"
        elif not any(" " in i for i in self.game_table) and not any("_" in i for i in self.game_table):
            return "Draw"

    def show_table(self):
        print("---------")
        print(f"| {self.game_table[0][0]} {self.game_table[0][1]} {self.game_table[0][2]} |")
        print(f"| {self.game_table[1][0]} {self.game_table[1][1]} {self.game_table[1][2]} |")
        print(f"| {self.game_table[2][0]} {self.game_table[2][1]} {self.game_table[2][2]} |")
        print("---------")


if __name__ == '__main__':
    TicTacToe().game_function()
