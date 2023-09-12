from manim import *
from numpy import ndarray


def fade_and_move_to_object(scene: Scene, from_object: Mobject, to_object: Mobject):
    # Move the text to the shape and fade it out
    scene.play(
        from_object.animate.move_to(to_object).fade(1),
    )


def fade_in_and_move_to_point(scene: Scene, from_object: Mobject, to_point: ndarray, delay: float):
    # Move the text to the shape and fade it out
    scene.play(FadeIn(from_object), from_object.animate.move_to(to_point))
    scene.wait(delay)
    scene.play(FadeOut(from_object))
