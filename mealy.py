from manim import *

from mealy_machine_library import function_type, mealy_machine_as_a_function, play_automaton_as_animation


class Introduction(Scene):
    def construct(self):
        # Cena de abertura

        self.wait(60)

        ab_word = Text("abba")
        binary_word = Text("0110")

        # Create the initial text and the target text

        # Set the initial position for the initial text with an offset
        ab_word.move_to(3 * LEFT)  # You can adjust the offset as needed
        binary_word.move_to(3 * RIGHT)

        # Add the initial text to the scene
        self.add(ab_word)

        # Use ReplacementTransform to morph the text and move it to the right
        self.play(
            ReplacementTransform(ab_word, binary_word),
        )

        # Wait for a moment before ending the scene
        self.wait(1)
        self.play(FadeOut(ab_word, binary_word))

        mealy_machine: Text = Text("Máquina de Mealy").scale(1.5)
        manim: Text = Text("Manim").scale(1.5)

        self.play(FadeIn(mealy_machine))
        self.wait(5)
        self.play(FadeOut(mealy_machine))
        self.play(FadeIn(manim))
        self.wait(3)
        self.play(FadeOut(manim))


class MealyMachineDefinition(Scene):
    def construct(self):
        self.finite_transductor_title()


        # Create the text and shape
        mealy_machine_as_a_function(self)

        mealy_machine_tuple(self)

        self.same_length_property()

    def same_length_property(self):
        input_word: Tex = Tex("$w_0$")
        self.play(Create(input_word))
        self.wait(3)
        input_word_length: Tex = Tex("$|w_0| = n$")
        self.play(ReplacementTransform(input_word, input_word_length))
        self.wait(3)
        output_word: Tex = Tex("$w_1$")
        self.play(ReplacementTransform(input_word_length, output_word))
        self.wait(3)
        output_word_length: Tex = Tex("$|w_1| = n$")
        self.play(ReplacementTransform(output_word, output_word_length))
        self.wait(3)
        self.play(FadeOut(output_word_length))

    def finite_transductor_title(self):
        finite_transductor = Text("Transdutor finito")
        self.play(Create(finite_transductor))
        self.wait(3)
        self.play(FadeOut(finite_transductor))


def mealy_machine_tuple(scene: Scene):
    empty_tuple: Tex = Tex("$()$")
    tuple_1_element: Tex = Tex("$(Q)$")
    tuple_2_element: Tex = Tex("$(Q, \Sigma)$")
    tuple_3_element: Tex = Tex("$(Q, \Sigma, \Gamma)$")
    tuple_4_element: Tex = Tex("$(Q, \Sigma, \Gamma, q_i)$")
    tuple_5_element: Tex = Tex("$(Q, \Sigma, \Gamma, q_i, \delta)$")
    tuple_6_element: Tex = Tex("$(Q, \Sigma, \Gamma, q_i, \delta, \Lambda)$")

    transition_function_definition = Tex(function_type("\sigma", "Q \times Sigma", "Q"))


    delta_definition: Tex = Tex(function_type("\sigma", "Q \\times \Sigma", "Q"))
    lambda_definition: Tex = Tex(function_type("\lambda", "Q \\times \Sigma", "\Gamma"))

    function_definitions: dict[int, Tex] = {
        5: delta_definition,
        6: lambda_definition
    }

    tuple_elements: list[Tex] = [tuple_1_element, tuple_2_element, tuple_3_element, tuple_4_element, tuple_5_element,
                      tuple_6_element]

    scene.play(Write(empty_tuple))

    current_element = empty_tuple
    current_function_definition: Tex | None = None

    for element, index in tuple_elements:
        if function_definitions.has_key(index):
            function_definition = function_definitions[index]
            scene.wait(2)
            if function_definition is not None:
                scene.play(function_definition)
            scene.play(ReplacementTransform(current_element, element))
            current_function_definition = function_definition
        current_element = element


class MealyMachineExample(MovingCameraScene):
    def construct(self):
        sample_mealy_machine_animation(self)

def sample_mealy_machine_animation(scene: Scene):
    q0_state = Tex("$q_0$")
    initial_state_marker = Triangle().rotate(60 * DEGREES)

    q1_state = Tex("$q_1$")
