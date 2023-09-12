from manim import *

from manim_animation_library import fade_and_move_to_object, fade_in_and_move_to_point


def function_type(function: str, domain: str, counterdomain: str):
    return Tex(f"${function} : {domain} \rightarrow {counterdomain} $")


def mealy_machine_as_a_function(scene: Scene):
    input_word = Text("abcde").move_to(4 * LEFT)
    mealy_machine: Text = Text("Máquina de Mealy").scale(0.5)
    mealy_machine_frame = Square(color=WHITE).surround(mealy_machine, 2)
    output_word: Mobject = Text("01001").move_to(mealy_machine)
    scene.add(mealy_machine_frame)
    scene.play(Write(input_word))
    scene.play(Create(mealy_machine))

    # Add text and shape to the scene
    fade_and_move_to_object(scene, input_word, mealy_machine)
    # Wait for a moment before ending the scene
    scene.wait(1)
    fade_in_and_move_to_point(scene, output_word, 4 * RIGHT, 1)

    scene.play(FadeOut(mealy_machine))

