from sys import flags
from manim import *
import os
import numpy as np

# # Obtenemos el direcotrio donde se trabaja
# cwd = os.getcwd() # /home/jupyter/Desktop/ProyectoA/ploting_and_data_tools

# # El archivo al que se dara lectura es cargado con el alias -file-
# # file = cwd+'/raman/CdSe4_04.txt'

# # TODO: Implementar este script para la lectura de todos los archivos en un directorio

# files = []

# for file in os.listdir(cwd + "/raman"):
#     if file.endswith(".txt"):
#         files.append(cwd+"/raman/"+file)

# # for file in files:
# #     print(file)

# # Leemos el archivo y lo ordenamos en una lista para su tratamiento

# # for i in range(0, len(files)):
# #     with open(files[i],'r') as f:
# #         cont = f.read()
# #         text = cont.split('#Acquired')[1].split('\n')[1:-1]
# #         print(text)
# #         print(" \n \n")

# spx = []
# spy = []

# with open(files[0],'r') as f:
#     cont = f.read()
#     values = cont.split('#Acquired')[1].split('\n')[1:-1]
#     for string_values in values:
#         x = float(string_values.split('\t')[0])
#         y = float(string_values.split('\t')[1])
#         spx.append(x)
#         spy.append(y)

# # print(spx)
# # print('\n')
# # print(spy)

# print(spx)

# class RamanSpectra(Scene):
#     def construct(self):
#         origin = Dot(ORIGIN)

class Graph(Scene):
    def construct(self):
        origin = Dot(ORIGIN,0.1)
        vg = VGroup(origin)
        x = np.random.random(10)
        y = np.random.random(10)
        x.sort()
        y.sort()
        for i in range(0,10):
            vg = VGroup(vg, Dot([x[i],y[i],0], 0.01))
        for i in range(0,9):
            init = Dot([x[i],y[i],0.01])
            endg = Dot([x[i+1],y[i+1],0.01])
            line = Line(init.get_center(),endg.get_center(), color=PURPLE).scale(0.1)
            vg = VGroup(vg, line)
        self.play(FadeIn(vg))
        self.wait(2)
        self.play(FadeOut(vg))



# print(x)
# print('\n')
# print(y)


# class VectorArrow(Scene):
#     def construct(self):
#         dot = Dot(ORIGIN) #
#         dot2= Dot([0,1,0], 0.01)
#         arrUP = Arrow(ORIGIN, [0, 2, 0], buff=0, stroke_width=1, max_tip_length_to_length_ratio=0.1) #
#         arrDO = Arrow(ORIGIN, [2, 0, 0], buff=0, stroke_width=1, max_tip_length_to_length_ratio=0.1) #
#         self.play(FadeIn(dot))
#         self.wait(2)
#         self.play(GrowArrow(arrUP))
#         self.wait(2)
#         self.play(GrowArrow(arrDO))
#         self.wait(2)
#         g = VGroup(dot, arrUP, arrDO)
#         gg = Dot([1,1,0], 0.01)
#         self.play(FadeIn(gg))
#         g = VGroup(g,gg)
#         self.play(FadeOut(g))
#         self.wait(1)
#         self.play(FadeIn(dot2))
#         self.wait(1)
#         circle = Circle(radius=1, color=BLUE)
#         dot = Dot()
#         dot2 = dot.copy().shift(RIGHT)
#         self.add(dot)
#         self.play(FadeOut(dot))
#         line = Line([3, 0, 0], [5, 0, 0])
#         self.add(line)
#         self.play(GrowFromCenter(circle))
#         self.play(Transform(dot, dot2))
#         self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
#         self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
#         self.wait()
