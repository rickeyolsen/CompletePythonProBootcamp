## Python Functions & Karel

### Instructions

On [Reeborg](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json), I was instructed to write functions to successfully complete the "Maze" room. I needed to utilize built-in functions while solving to "turn right". I also needed to utilize a while loop as well as if/elif/else statements to accomplish the task.

### Code Written on Reeborg

'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_on_right():
        if wall_in_front():
            turn_left()
        else:
            move()
    elif wall_on_right() == 0:
        turn_right()
        if wall_in_front() == 0:
            move()
'''