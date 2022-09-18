from manimlib import *

class MyBeautifulGraph(Scene):
    def construct(self):
        x = [0, 1, 2, 3, 4]
        y = [1, 2, 4, 2, 3]
        axes = Axes(x, y, add_vertex_dots=True)
        self.add(axes)