from manim import Tex


def function_type(function: str, domain: str, counterdomain: str):
    return Tex(f"${function} : {domain} \rightarrow {counterdomain} $")


