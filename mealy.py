from manim import *

from mealy_machine_library import function_type, mealy_machine_as_a_function


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

        self.same_length_property()

        # Create the text and shape
        mealy_machine_as_a_function(self)

        mealy_machine_tuple(self)

        transition_function_definition = Tex(function_type("sigma", "Q \times Sigma", "Q"))

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
    empty_tuple = Tex("$()$")
    tuple_1_element = Tex("$(Q)$")
    tuple_2_element = Tex("$(Q, \Sigma)$")
    tuple_3_element = Tex("$(Q, \Sigma, q_i)$")
    tuple_4_element = Tex("$(Q, \Sigma, q_i, \Delta)$")
    tuple_5_element = Tex("$(Q, \Sigma, q_i, \Delta, \sigma)$")
    tuple_6_element = Tex("$(Q, \Sigma, q_i, \Delta, \sigma, \Lambda)$")

    tuple_elements = [tuple_1_element, tuple_2_element, tuple_3_element, tuple_4_element, tuple_5_element,
                      tuple_6_element]

    scene.play(Write(empty_tuple))

    current_element = empty_tuple

    for element in tuple_elements:
        scene.wait(2)
        scene.play(ReplacementTransform(current_element, element))
        current_element = element


class MealyMachineExample(Scene):
    def construct(self):
        # Defina seus estados, transições e funções de saída aqui
        states = ["q_0", "q_1"]
        transitions = [((0, "q0"), "q1"), ((1, "q0"), "q1"), ((0, "q1"), "q0"), ((1, "q1"), "q0")]
        outputs = [((0, "q0"), "a"), ((1, "q0"), "b"), ((0, "q1"), "a"), ((1, "q1"), "a")]

        input_string = "0110"
        output_string = ""

        states_tex = [Tex(estado) for estado in states]
        states_group = VGroup(*states_tex)
        states_group.arrange(RIGHT, buff=1.5)

        current_state_tex = Tex("q_0", color=GREEN)
        current_state_tex.next_to(states_tex[0], UP)

        self.play(Create(states_group))
        self.play(Create(current_state_tex))

        output_symbols_group = VGroup()  # Grupo para armazenar os símbolos de saída
        arrows_group = VGroup()  # Grupo para armazenar as setas de transição

        proximo_estado: str | None = None

        for simbolo in input_string:
            for transicao in transitions:
                if (int(simbolo), current_state_tex.get_text()) == transicao[0]:
                    proximo_estado = transicao[1]
                    break

            # Atualize o estado atual
            proximo_estado_text = Text(proximo_estado, color=GREEN)
            proximo_estado_text.next_to(states_tex[states.index(proximo_estado)], UP)

            # Crie uma seta para representar a transição
            seta = Arrow(current_state_tex, proximo_estado_text, buff=0.1)
            arrows_group.add(seta)

            # Determine a saída com base na função de saída
            for saida in outputs:
                if (int(simbolo), current_state_tex.get_text()) == saida[0]:
                    simbolo_saida = saida[1]
                    break

            # Atualize a palavra de saída
            output_string += simbolo_saida

            # Crie animações para mostrar a saída na tela
            simbolo_saida_text = Text(simbolo_saida)  # Alinhamento na parte inferior
            if output_symbols_group:
                simbolo_saida_text.next_to(output_symbols_group, RIGHT, buff=0.2)  # Espaçamento entre símbolos
            else:
                simbolo_saida_text.next_to(current_state_tex, DOWN, buff=0.2)  # Espaçamento entre símbolos
            output_symbols_group.add(simbolo_saida_text)

            # Animação de transição e saída
            self.play(
                Transform(current_state_tex, proximo_estado_text),
                Create(seta),
                Create(simbolo_saida_text)
            )
            self.wait(0.5)

        # Exiba a palavra de saída final
        palavra_saida_texto = Text(output_string)  # Alinhamento na parte inferior
        palavra_saida_texto.next_to(current_state_tex, DOWN, buff=0.2)  # Espaçamento entre símbolos
        self.play(Create(palavra_saida_texto))
        self.wait()
