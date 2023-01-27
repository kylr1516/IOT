class Trace:
    def __init__(self, screen):
        self.screen = screen
        # init demo/game specific variables here

    # Draws or erases a 0 based on the position given
    def draw_0(self, position, draw):
        drawpos=0
        if draw == True:
            value = 15
            combine = True
        else:
            value = 0
            combine = False
        if position==3:
            drawpos=4
