from ctypes import alignment
from manim import *
import cv2

def animate_gif(scene, 
                file_name,
                scale = 1, 
                wait_time=.07,
                modify = lambda img: img): 
  cap = cv2.VideoCapture(file_name)
  flag = True
  while flag :
    flag, frame = cap.read()
    if flag:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_img = ImageMobject(frame).scale(scale)
        modify(frame_img)
        scene.add(frame_img)
        scene.wait(wait_time)
        scene.remove(frame_img)

  cap.release()


class Presentacion(Scene):

    def construct(self):

        # ============================= C O N S T A N T S =============================
        # =============================================================================

        # Configurando el fondo
        self.camera.background_color = "#071F37"

        # Test colors
        col1 = "#87c2a5"
        col2 = "#525893"
        col3 = "#e07a5f"
        col4 = "#343434"

        # =============================================================================
        # =============================================================================

        l1 = MathTex(r'\textrm{Fourier Analysis on Raman Spectroscopy:}')
        l2 = MathTex(r'\textrm{Denoising and Data Analysis procedures}')
        title = VGroup(l1,l2)
        title.scale(1.5)
        title.arrange(DOWN)

        # =============================================================================
        # =============================================================================

        p1 = Text("""        In 1809 Joseph Fourier developed a theory
        that provide insights in the signal field.
        After this succeed, a trigonometric rep. 
        of a function was possible to obtain and 
        that representation gives us information 
        about the frequency domain""",font_size=24, font='Monospace')

        # =============================================================================
        # ===================*=================*======================*================

        p2 = Text("""        Frequently we encounter functions that can
        be analyzed on another space different
        than the space were we see the signal""",font_size=24, font='Monospace')

        # =============================================================================
        # ===================*=================*======================*================

        int_transform = MathTex(r'F(\alpha) = \int_{\Omega} f(t) K(\alpha, t) \: dt')

        # =============================================================================
        # ===================*=================*======================*================


        # =============================================================================
        # ===================*=================*======================*================
        
        
        # =============================================================================
        # ===================*=================*======================*================
        
        
        # =============================================================================
        # ===================*=================*======================*================



        obsmatrix = MathTex(r"""
        X = \begin{bmatrix}
         |  &  |  & |  \\
        x_1 & ... & x_n\\
         |  &  |  & |
        \end{bmatrix}
        """)


        # ============================= C O N S T A N T S =============================
        # =============================================================================
        # =============================================================================
        # =============================================================================


        self.play(Write(title))
        self.wait(5)
        self.play(Unwrite(title))

        self.wait(2)

        self.play(Write(p1))
        self.play(p1.animate.to_corner(UP+LEFT))
        self.wait(2)
        self.play(Write(p2))
        self.play(p2.animate.to_corner(DOWN+RIGHT))
        self.play(Write(int_transform))
        self.play(Unwrite(p1))
        self.play(Unwrite(p2))
        self.play(FadeOut(int_transform))

        c = Circle(2)
        self.play(FadeIn(c))
        self.wait(2)
        self.play(FadeOut(c))

        animate_gif(self, "fourier_conv.gif", scale = 2 , modify = lambda frm : frm.to_corner(UR))
        
        s = Square(3)
        self.play(FadeIn(s))
        self.wait(2)
        self.play(FadeOut(s))

        self.wait(2)
        self.add(Circle())
        self.clear()
        self.play(Write(obsmatrix))
        self.wait(2)
