from pico2d import *
from boy import Boy
from ball import Ball
from grass import Grass

import game_world

# Game object class here


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)
            if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                ball_x = boy.x + boy.face_dir * 45
                game_world.add_object(
                    Ball(ball_x, boy.y - 35, boy.face_dir)
                )



def reset_world():
    global boy

    boy = Boy()
    game_world.add_object(boy, 1)

    grass = Grass()
    game_world.add_object(grass)


def update_world():
    game_world.update()
    pass


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


running = True



open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
