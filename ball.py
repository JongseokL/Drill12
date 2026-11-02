from pico2d import get_canvas_height, get_canvas_width, load_image

import game_world


class Ball:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.velocity_y = 7
        self.image = load_image('ball21x21.png')

    def update(self):
        self.x += self.direction * 8
        self.y += self.velocity_y
        self.velocity_y -= 0.25

        if (self.x < -11 or self.x > get_canvas_width() + 11 or
                self.y < -11 or self.y > get_canvas_height() + 11):
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
