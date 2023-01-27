class Trace:
    def __init__(self, screen):
        self.screen = screen
        # init demo/game specific variables here

    # Draws or erases a 0 based on the position given
    def draw_0(self, position, draw):
        if draw == True:
            value = 15
            combine = True
        else:
            value = 0
            combine = False
        if position == 3:
            for i in range(8):
                self.screen.draw_pixel(i + 4, 8, value, combine, False)
            for i in range(32):
                self.screen.draw_pixel(4, i + 9, value, combine, False)
            for i in range(8):
                self.screen.draw_pixel(i + 4, 48 - 8, value, combine, False)
            for i in range(32):
                self.screen.draw_pixel((3 + 8), i + 9, value, combine, False)
            self.screen.push()
        if position == 2:
            for i in range(8):
                self.screen.draw_pixel(i + 14, 8, value, combine, False)
            for i in range(32):
                self.screen.draw_pixel(14, i + 9, value, combine, False)
            for i in range(8):
                self.screen.draw_pixel(i + 14, 48 - 8, value, combine, False)
            for i in range(32):
                self.screen.draw_pixel((13 + 8), i + 9, value, combine, False)
            self.screen.push()
        if position == 1:
            for i in range(8):
                self.screen.draw_pixel(i + 27, 8, value, combine, False)
            for i in range(32):
                self.screen.draw_pixel(27, i + 9, value, combine, False)
            for i in range(8):
                self.screen.draw_pixel(i + 27, 48 - 8, value, combine, False)
            for i in range(32):
                self.screen.draw_pixel((26 + 8), i + 9, value, combine, False)
            self.screen.push()
        if position == 0:
            for i in range(8):
                self.screen.draw_pixel(i + 37, 8, value, combine, False)
            for i in range(32):
                self.screen.draw_pixel(37, i + 9, value, combine, False)
            for i in range(8):
                self.screen.draw_pixel(i + 37, 48 - 8, value, combine, False)
            for i in range(32):
                self.screen.draw_pixel((36 + 8), i + 9, value, combine, False)
            self.screen.push()