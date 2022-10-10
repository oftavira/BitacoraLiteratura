from manim import *

class CreateCircle(Scene):
    def construct(self):
        # Configurando el fondo
        self.camera.background_color = "#6c1d45"

        # Test colors
        col1 = "#87c2a5"
        col2 = "#525893"
        col3 = "#e07a5f"
        col4 = "#343434"

        # MANIM: INiciamos una escena vacia con color de fondo guinda
        # almacenamos tambien colores a disposiciòn

        # MANIM: Empezamos la construcciòn de un circulo sin renderizar
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        # MANIM: Se hace fade in al circulo
        self.play(FadeIn(circle))  # show the circle on screen
        self.play(circle.animate.to_corner())

        # MANIM: Creacion y movimiento de una letra

        ds_m = MathTex(r"\mathbb{M}", fill_color=col4)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)

        self.play(FadeIn(ds_m))
        self.play(ds_m.animate.to_corner(corner=UP+RIGHT))

        circle2 = Circle(color=col1, fill_opacity=1).shift(LEFT)
        self.play(FadeIn(circle2))
        self.play(circle2.animate.to_corner(corner=UP+LEFT))


        square = Square(color=col2, fill_opacity=1).shift(UP)
        self.play(FadeIn(square))
        self.play(square.animate.to_corner(corner=DOWN+RIGHT))


        triangle = Triangle(color=col3, fill_opacity=1).shift(RIGHT)
        self.play(FadeIn(triangle))
        self.wait(2)

        logo = VGroup(triangle, square, circle, ds_m, circle2)  # order matters
        self.play(FadeOut(logo))

        corona= ImageMobject("van_gogh.jpeg")
        self.play(FadeIn(corona))
        self.play(corona.animate.to_edge(RIGHT, buff=1))
        self.play(corona.animate.scale(0.2))
        self.play(FadeOut(corona))


