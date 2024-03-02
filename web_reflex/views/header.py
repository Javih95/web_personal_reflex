import reflex as rx
from web_reflex.styles.styles import Size,TextColor, MAX_WIDTH_STYLE
import web_reflex.constantes as constantes

def header() -> rx.component:
    return rx.vstack(
        rx.heading(
            "Bienvenido a mi espacio digital",
            size = "lg",
            padding_bottom = Size.DEFAULT.value
        ),
        rx.flex(
            rx.image(
                src= "mouredev.png",
                alt= "Avatar",
                width= "16em",
                heigth = "16em",
                margin_right = Size.BIG.value
            ),
            rx.vstack(
                rx.box(
                    rx.text("Soy CtrlJ,desarrollador de software"),
                    rx.text("enfocado en la creación de soluciones innovadoras")
                ),
                rx.span("Explora ",
                         rx.span("mi portafolio",color =TextColor.DESTACAR.value),
                         " para descubrir proyectos emocionantes"),
                rx.span("conoce mis habilidades técnicas "),
                rx.span("y únete a mí en el viaje de la programación"),
                rx.link(
                    "linkedin",
                    href=constantes.LINKEDIN_URL,
                    is_external= True,
                    color = TextColor.TERCIARIO.value,
                    paddin_top = Size.BIG.value,
                    font_size = Size.MEDIUM.value
                    ),
                align_items="start",
            ),
            flex_direction =["column","column","column","row","row"]
        ),
        padding_top = Size.VERY_BIG.value,
        style= MAX_WIDTH_STYLE
    )