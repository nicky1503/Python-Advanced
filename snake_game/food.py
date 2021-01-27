import config
from random import randrange

food_pos = [randrange(0, config.WINDOW_WIDTH-config.SCALE, config.SCALE), randrange(0, config.WINDOW_HEIGHT-config.SCALE, config.SCALE)]

def show():
    fill(255, 0, 0)
    rect(food_pos[0], food_pos[1], config.SCALE, config.SCALE)
    


def reset():
    food_pos[0] = randrange(0, config.WINDOW_WIDTH-config.SCALE, config.SCALE)
    food_pos[1] = randrange(0, config.WINDOW_HEIGHT-config.SCALE, config.SCALE)
    
