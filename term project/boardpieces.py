class Settlement(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.size = 10
        self.color = color
    
    def draw(self, canvas):
        points = [(x - self.size, y + self.size),(x + self.size, y + self.size),(x + self.size, y - self.size),(x, y - 2* self.size),(x - self.size, y - self.size)]
        canvas.create_polygon(points, fill = self.color)
        
        