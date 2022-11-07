from manim import *

""" class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        ).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)
        bool_ops_text = MarkupText("<u>Boolean Operation</u>").next_to(ellipse1, UP * 3)
        ellipse_group = Group(bool_ops_text, ellipse1, ellipse2).move_to(LEFT * 3)
        self.play(FadeIn(ellipse_group))

        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
        intersection_text = Text("Intersection", font_size=23).next_to(i, UP)
        self.play(FadeIn(intersection_text))

        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("Union", font_size=23)
        self.play(u.animate.scale(0.3).next_to(i, DOWN, buff=union_text.height * 3))
        union_text.next_to(u, UP)
        self.play(FadeIn(union_text))

        e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        exclusion_text = Text("Exclusion", font_size=23)
        self.play(e.animate.scale(0.3).next_to(u, DOWN, buff=exclusion_text.height * 3.5))
        exclusion_text.next_to(e, UP)
        self.play(FadeIn(exclusion_text))

        d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
        difference_text = Text("Difference", font_size=23)
        self.play(d.animate.scale(0.3).next_to(u, LEFT, buff=difference_text.height * 3.5))
        difference_text.next_to(d, UP)
        self.play(FadeIn(difference_text))
 """
# class Lasers(Scene):
#     def construct(self):
#         # difference_text = Text("Difference", font_size=23)
#         # comp_text       = Text("Comp", font_size=23)
#         # self.wait(2)
#         # comp_text.next_to(difference_text, DOWN)
#         # self.play(FadeIn(difference_text))
#         # self.play(Write(comp_text))
#         # self.wait(2)
#         p = NumberPlane()
#         self.play(FadeIn(p))
#         self.wait(2)
#         comp_text = Text("Comp", font_size=23)
#         self.play(Write(comp_text))
#         self.wait(2)
#         self.play(p.scale(0.2))
#         self.wait(2)

# def graphasvgroup(arr,size):


class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN) #
        dot2= Dot([0,1,0], 0.01)
        arrUP = Arrow(ORIGIN, [0, 2, 0], buff=0, stroke_width=1, max_tip_length_to_length_ratio=0.1) #
        arrDO = Arrow(ORIGIN, [2, 0, 0], buff=0, stroke_width=1, max_tip_length_to_length_ratio=0.1) #
        self.play(FadeIn(dot))
        self.wait(2)
        self.play(GrowArrow(arrUP))
        self.wait(2)
        self.play(GrowArrow(arrDO))
        self.wait(2)
        g = VGroup(dot, arrUP, arrDO)
        self.play(FadeOut(g))
        self.wait(1)
        self.play(FadeIn(dot2))
        self.wait(1)
        circle = Circle(radius=1, color=BLUE)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)
        self.play(FadeOut(dot))
        line = Line([3, 0, 0], [5, 0, 0])
        self.add(line)
        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
        self.wait()
