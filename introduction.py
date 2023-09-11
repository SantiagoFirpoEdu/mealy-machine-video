from manim import *


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

        # Create the text and shape
        input_word = Text("abcde").move_to(4 * LEFT)
        output_word = Text("01001").move_to(4 * RIGHT)

        mealy_machine_frame = Square(color=WHITE)
        mealy_machine = Text("Máquina de Mealy").surround(mealy_machine_frame)

        self.play(Write(input_word))
        self.play(Create(mealy_machine))

        # Add text and shape to the scene
        fade_and_move_to(self, input_word, mealy_machine)

        # Wait for a moment before ending the scene
        self.wait(1)

        mealy_machine_tuple(self)

        transition_function_definition = Tex(function_type("sigma", "Q \times Sigma", "Q"))

    def finite_transductor_title(self):
        finite_transductor = Text("Transdutor de estado finito")
        self.play(Create(finite_transductor))
        self.wait(3)
        self.play(FadeOut(finite_transductor))


def fade_and_move_to(scene: Scene, from_object: Mobject, to_object: Mobject):
    # Move the text to the shape and fade it out
    scene.play(
        from_object.animate.move_to(to_object).fade(1),
    )


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


def function_type(function: str, domain: str, counterdomain: str):
    return Tex(f"${function} : {domain} \rightarrow {counterdomain} $")


class MealyMachineExample(Scene):
    def construct(self):
        # Defina seus estados, transições e funções de saída aqui
        estados = ["q0", "q1"]
        transicoes = [((0, "q0"), "q1"), ((1, "q0"), "q1"), ((0, "q1"), "q0"), ((1, "q1"), "q0")]
        saidas = [((0, "q0"), "a"), ((1, "q0"), "b"), ((0, "q1"), "a"), ((1, "q1"), "a")]

        # Insira a palavra de entrada
        palavra_entrada = "0110"
        palavra_saida = ""

        # Crie a representação visual da máquina de Mealy
        estados_text = [Text(estado) for estado in estados]
        estados_group = VGroup(*estados_text)
        estados_group.arrange(RIGHT, buff=1.5)  # Espaçamento entre estados

        # Crie um estado atual
        estado_atual = Text("q0", color=GREEN)
        estado_atual.next_to(estados_text[0], UP)

        # Adicione estados à cena
        self.play(Create(estados_group))
        self.play(Create(estado_atual))

        # Crie as animações para a transição e saída da palavra
        simbolos_saida_group = VGroup()  # Grupo para armazenar os símbolos de saída
        setas_group = VGroup()  # Grupo para armazenar as setas de transição

        for simbolo in palavra_entrada:
            # Determine a próxima transição com base no símbolo de entrada
            for transicao in transicoes:
                if (int(simbolo), estado_atual.get_text()) == transicao[0]:
                    proximo_estado = transicao[1]
                    break

            # Atualize o estado atual
            proximo_estado_text = Text(proximo_estado, color=GREEN)
            proximo_estado_text.next_to(estados_text[estados.index(proximo_estado)], UP)

            # Crie uma seta para representar a transição
            seta = Arrow(estado_atual, proximo_estado_text, buff=0.1)
            setas_group.add(seta)

            # Determine a saída com base na função de saída
            for saida in saidas:
                if (int(simbolo), estado_atual.get_text()) == saida[0]:
                    simbolo_saida = saida[1]
                    break

            # Atualize a palavra de saída
            palavra_saida += simbolo_saida

            # Crie animações para mostrar a saída na tela
            simbolo_saida_text = Text(simbolo_saida)  # Alinhamento na parte inferior
            if simbolos_saida_group:
                simbolo_saida_text.next_to(simbolos_saida_group, RIGHT, buff=0.2)  # Espaçamento entre símbolos
            else:
                simbolo_saida_text.next_to(estado_atual, DOWN, buff=0.2)  # Espaçamento entre símbolos
            simbolos_saida_group.add(simbolo_saida_text)

            # Animação de transição e saída
            self.play(
                Transform(estado_atual, proximo_estado_text),
                Create(seta),
                Create(simbolo_saida_text)
            )
            self.wait(0.5)

        # Exiba a palavra de saída final
        palavra_saida_texto = Text(palavra_saida)  # Alinhamento na parte inferior
        palavra_saida_texto.next_to(estado_atual, DOWN, buff=0.2)  # Espaçamento entre símbolos
        self.play(Create(palavra_saida_texto))
        self.wait()
