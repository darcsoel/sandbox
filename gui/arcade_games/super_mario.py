import arcade
import time
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
JUMP_HEIGHT = 140
MOVE_SPEED = 100
MIN_HEIGHT = 100


class MarioWindow(arcade.Window):
    def _create_coin(self, index):
        coin = arcade.Sprite('images/gold.png', 0.1)
        coin.center_y = MIN_HEIGHT + randint(110, 220)
        coin.center_x = index * 140
        self.coin_list.append(coin)

    def _create_ground(self, index):
        ground = arcade.Sprite('images/ground.png', 0.5)
        ground.center_y = 90
        ground.center_x = index * MIN_HEIGHT
        self.ground_list.append(ground)

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title='Super Mario Game')
        arcade.set_background_color(arcade.color.ANDROID_GREEN)

        self.score = 0

        self.coin_list = arcade.SpriteList()
        self.ground_list = arcade.SpriteList()

        self.player = arcade.Sprite("images/mario_run.png", 0.1)
        self.player.center_y = 150
        self.player.center_x = MIN_HEIGHT

        for i in range(0, 9):
            self._create_ground(i)

        for i in range(1, 6):
            self._create_coin(i)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.coin_list)

    def on_draw(self):
        """Render the screen. """

        arcade.start_render()

        self.player.draw()
        self.coin_list.draw()
        self.ground_list.draw()

        # Put the text on the screen.
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W or symbol == arcade.key.SPACE:
            self.player.center_y += JUMP_HEIGHT
        if symbol == arcade.key.A and self.player.center_x > 0:
            self.player.center_x -= MOVE_SPEED
        if symbol == arcade.key.D and self.player.center_x < SCREEN_WIDTH:
            self.player.center_x += MOVE_SPEED

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W or symbol == arcade.key.SPACE:
            time.sleep(0.1)
            self.player.center_y -= JUMP_HEIGHT

    def update(self, delta_time: float):
        self.physics_engine.update()

        self.coin_list.update()
        hit = arcade.check_for_collision_with_list(self.player, self.coin_list)

        for coin in hit:
            self.score += 1
            coin.kill()

        coins_count = len(self.coin_list)
        if coins_count < 3:
            self._create_coin(randint(1, 5))


if __name__ == '__main__':
    window = MarioWindow()
    arcade.run()
