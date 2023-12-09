from manim import *

RED = "#FF644E"
BLUE = "#00a2ff"

class CircleToFlower(Scene):
	def construct(self):
		# draw circle
		circle = Circle(radius=2, color=WHITE, stroke_width=10)
		# flip circle on its head
		circle.flip(UP)
		circle.rotate(PI)
		self.add(circle)
		self.wait(1)
		# morph circle to flower svg
		flower = SVGMobject("flower.svg", stroke_width=10, stroke_color=RED, fill_color=RED, fill_opacity=.25).scale(2)
		flower.shift(DOWN*.37)
		self.play(Transform(circle, flower), run_time=3)
		self.wait(1)


class CircleToTriangle(Scene):
	def construct(self):
		# draw circle
		circle = Circle(radius=.1, color=WHITE, fill_opacity=1)
		# flip circle on its head
		circle.flip(UP)
		circle.rotate(PI)
		self.add(circle)
		self.wait(1)
		# morph circle to triangle svg
		triangle = SVGMobject("triangle.svg", stroke_width=10, stroke_color=BLUE, fill_color=BLUE, fill_opacity=.25).scale(2)
		triangle.shift(UP*.65)
		self.play(Transform(circle, triangle), run_time=3)
		self.wait(1)