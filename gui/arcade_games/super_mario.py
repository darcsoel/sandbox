import arcade
import time
from random import randint

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
JUMP_HEIGHT = 160
MOVE_SPEED = 100
MIN_HEIGHT = 150
MIN_WIDTH = 150
GROUND_BLOCKS_DISTANCE = 100
GROUND_BLOCKS_COUNT = 11
GROUND_HEIGHT = 80
COINS_COUNT = 6
COINS_DISTANCE = 140


class MarioWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title='Super Mario Game')
        arcade.set_background_color(arcade.color.AZURE)

        self.score = 0

        self.coin_list = arcade.SpriteList()
        self.ground_list = arcade.SpriteList()

        self.player = arcade.Sprite("images/mario_run.png", 0.1)
        self.player.center_y = MIN_HEIGHT
        self.player.center_x = MIN_WIDTH

        for i in range(0, GROUND_BLOCKS_COUNT):
            self._create_ground(i)

        for i in range(1, COINS_COUNT):
            self._create_coin(i)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.coin_list)

    def _create_coin(self, index):
        coin = arcade.Sprite('images/gold.png', 0.1)
        coin.center_y = MIN_HEIGHT + randint(110, 220)
        coin.center_x = index * COINS_DISTANCE
        self.coin_list.append(coin)

    def _create_ground(self, index):
        ground = arcade.Sprite('images/ground.png', 0.5)
        ground.center_y = GROUND_HEIGHT
        ground.center_x = index * GROUND_BLOCKS_DISTANCE
        self.ground_list.append(ground)

    def on_draw(self):
        """Render the screen. """

        arcade.start_render()

        self.player.draw()
        self.coin_list.draw()
        self.ground_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 10, arcade.color.ORANGE, 18)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W or symbol == arcade.key.SPACE:
            self.player.center_y += JUMP_HEIGHT
        elif symbol == arcade.key.A and self.player.center_x > MIN_WIDTH:
            self.player.center_x -= MOVE_SPEED
        elif symbol == arcade.key.D and self.player.center_x + MIN_WIDTH < SCREEN_WIDTH:
            self.player.center_x += MOVE_SPEED
        else:
            return

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W or symbol == arcade.key.SPACE:
            time.sleep(0.1)
            self.player.center_y = MIN_WIDTH

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
