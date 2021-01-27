import config
import snake
import food

def setup():
    size(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    frameRate(10)


def draw():
    background(0)
    snake.show()
    snake.move()
    snake.check_edges() 
    food.show()
    
    if snake.touches_food():
        snake.eat_food()
        food.reset()

        


def keyPressed():
    if keyCode == UP and config.CURRENT_DIR != "down":
        config.CURRENT_DIR = "up" 
    elif keyCode == DOWN and config.CURRENT_DIR != "up":
        config.CURRENT_DIR = "down"
    elif keyCode == LEFT and config.CURRENT_DIR != "right":
         config.CURRENT_DIR = "left"
    elif keyCode == RIGHT and config.CURRENT_DIR != "left":
        config.CURRENT_DIR = "right"
