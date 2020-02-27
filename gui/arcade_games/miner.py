import random
import arcade

ROW_COUNT = 15
COLUMN_COUNT = 15
WIDTH = 30
HEIGHT = 30
MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + 10 * MARGIN

NOT_PRESSED = {'code': 0, 'color': arcade.color.WHITE}
PRESSED_NEGATIVE = {'code': 1, 'color': arcade.color.YELLOW}
BOMB_DEACTIVATED = {'code': 2, 'color': arcade.color.GREEN}
BOMB_ACTIVE = {'code': 3, 'color': arcade.color.WHITE}
BOMB_FAILED = {'code': 4, 'color': arcade.color.RED}
BOMB_MAYBE_PRESENT = {'code': 5, 'color': arcade.color.ORANGE}


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.shape_list = None
        self.bomb_count = random.randint(5, 10)
        self.grid = []

        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(BOMB_ACTIVE['code'] if random.randint(5, 10) == 7 else NOT_PRESSED['code'])

        arcade.set_background_color(arcade.color.BLACK)
        self.recreate_grid()

    def recreate_grid(self):
        self.shape_list = arcade.ShapeElementList()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == NOT_PRESSED['code']:
                    color = NOT_PRESSED['color']
                elif self.grid[row][column] == PRESSED_NEGATIVE['code']:
                    color = PRESSED_NEGATIVE['color']
                elif self.grid[row][column] == BOMB_DEACTIVATED['code']:
                    color = BOMB_DEACTIVATED['color']
                elif self.grid[row][column] == BOMB_ACTIVE['code']:
                    color = BOMB_ACTIVE['color']
                elif self.grid[row][column] == BOMB_MAYBE_PRESENT['code']:
                    color = BOMB_MAYBE_PRESENT['color']
                else:
                    color = BOMB_FAILED['color']

                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                current_rect = arcade.create_rectangle_filled(x, y, WIDTH, HEIGHT, color)
                self.shape_list.append(current_rect)

    def on_draw(self):
        arcade.start_render()
        self.shape_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        col = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        if row < ROW_COUNT and col < COLUMN_COUNT:
            if self.grid[row][col] == NOT_PRESSED['code']:
                self.grid[row][col] = PRESSED_NEGATIVE['code']

                for i in range(row - 2, row + 2):
                    for j in range(col - 2, col + 2):
                        if BOMB_ACTIVE['code'] in self.grid[i] and self.grid[i][j] == NOT_PRESSED['code']:
                            self.grid[i][j] = BOMB_MAYBE_PRESENT['code']

            if self.grid[row][col] in [BOMB_ACTIVE['code'], BOMB_MAYBE_PRESENT['code']]:
                if button == arcade.MOUSE_BUTTON_LEFT:
                    self.grid[row][col] = BOMB_FAILED['code']
                if button == arcade.MOUSE_BUTTON_RIGHT:
                    self.grid[row][col] = BOMB_DEACTIVATED['code']

        self.recreate_grid()


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
