from distutils.errors import DistutilsFileError
from manim import *
import cv2, wget

"""
========================   S C E N E  _  C O N S T A N T S  _  A N D  _  U T I L S  ============================
"""
# SPEC: Utilidad para gifs 

# For more than one rep try : 
# ident while and add...
#       for i in range(0,repetitions):
#         cap = cv2.VideoCapture(file_name)
#         flag = True

def animate_gif(scene, 
                file_name, 
                wait_time=.07, 
                repetitions=1,
                modify = lambda img: img): 
  cap = cv2.VideoCapture(file_name)
  flag = True

  while flag :
    flag, frame = cap.read()
    if flag:
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      frame_img = ImageMobject(frame)
      modify(frame_img)
      scene.add(frame_img)
      scene.wait(wait_time)
      scene.remove(frame_img)

  cap.release()

# MANIM: Tex Objects
svd_m = Tex("""
        $$
        \\begin{vmatrix}
         |  &  |  & |  \\\\
        x_1 & ... & x_n\\\\
         |  &  |  & |
        \\end{vmatrix}
        $$
        """)


# MANIM: Images
raman = ImageMobject('abs.jpg')


# MANIM: COLORS
deep_blue = "#071F37"
deep_gui1 = "#260319"
deep_gui2 = "#370724"

"""
========================   S C E N E  _  C O N S T A N T S  _  A N D  _  U T I L S  ============================
"""

class MyScene(Scene):

    def construct(self):
      wget.download("https://media3.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif")
      animate_gif(self, "giphy.gif", 
                  modify = lambda frm: frm.to_corner(UR)
                  )










