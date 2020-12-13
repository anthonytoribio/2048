"""Creates the actual board and game using tkinter."""
#Will update the game so that utilizing an algorithm it should show the user
#the best possible move.

from tkinter import Frame, Label, CENTER
import random

import movements as logic
import constants as c


def gen():
    return random.randint(0, c.grid_len -1)


class GameGrid(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)

        self.commands = {c.k_up: logic.moveUp, c.k_down: logic.moveDown,
                         c.k_left: logic.moveLeft, c.k_right: logic.moveRight,
                         c.k_up_alt: logic.moveUp, c.k_down_alt: logic.moveDown,
                         c.k_left_alt: logic.moveLeft, c.k_right_alt: logic.moveRight}
        
        self.grid_cells = []
        self.init_grid()
        self.matrix = logic.new_game(c.grid_len)
        self.history_matrixs = []
        self.update_grid_cells()

        self.mainloop()


    def init_grid(self):
        background = Frame(self, bg = c.bk_color_game,
                           width = c.size, height = c.size)
        background.grid()

        for i in range(c.grid_len):
            grid_row = []
            for j in range(c.grid_len):
                cell = Frame(background, bg = c.bk_color_cell_empty,
                             width = c.size / c.grid_len,
                             height = c.size / c.grid_len)
                cell.grid(row = i, column = j, padx = c.grid_padding,
                          pady = c.grid_padding)
                t = Label(master = cell, text = "",
                          bg = c.bk_color_cell_empty,
                          justify = CENTER, font = c.font, width = 5, height = 2)
                t.grid()
                grid_row.append(t)

                
            self.grid_cells.append(grid_row)


    def update_grid_cells(self):
        for i in range(c.grid_len):
            for j in range(c.grid_len):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text = "", bg = c.bk_color_cell_empty)
                else:
                    self.grid_cells[i][j].configure(text = str(new_number), bg = c.bk_color_dict[new_number],
                                                   fg = c.cell_color_dict[new_number])
        self.update_idletasks()


    def key_down(self, event):
        key = repr(event.char)
        if key == c.k_back and len(self.history_matrixs) > 1:
            self.matrix = self.history_matrixs.pop()
            self.update_grid_cells()
            print('back on step total step:', len(self.history_matrixs))
        elif key in self.commands:
            self.matrix, done = self.commands[repr(event.char)](self.matrix)
            if done:
                self.matrix = logic.add_two(self.matrix)
                self.history_matrixs.append(self.matrix)
                self.update_grid_cells()
                if logic.game_state(self.matrix) == 'win':
                    self.grid_cells[1][1].configure(text = 'You', bg = c.bk_color_cell_empty)
                    self.grid_cells[1][2].configure(text = 'Win!', bg = c.bk_color_cell_empty)
                if logic.game_state(self.matrix) == 'lose':
                    self.grid_cells[1][1].configure(text = 'You', bg = c.bk_color_cell_empty)
                    self.grid_cells[1][2].configure(text = 'Lose!', bg = c.bk_color_cell_empty)


    def generate_next(self):
        index = (gen(), gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (gen(), gen())
        self.matrix[index[0]][index[1]] = 2


game_grid = GameGrid()
            


