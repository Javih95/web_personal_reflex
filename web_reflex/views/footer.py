import reflex as rx
from web_reflex.styles.styles import Size, MAX_WIDTH_STYLE,TextColor
import web_reflex.constantes as constantes
def footer() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "© 2023 CtrlJ. Todos los derechos reservados.",
                font_size = Size.MEDIUM.value,
                margin_button = Size.SMALL.value
                ),
            rx.link(
                "CtrlJ - Desarrollador Web",
                href= constantes.LINKEDIN_URL,
                font_size = Size.MEDIUM.value,
                color = TextColor.TERCIARIO.value,
                is_external= True

                ),
            aling_items = "start",
            spacing= Size.MEDIUM.value
        ),
        rx.spacer(),
        rx.image(
            src= "mouredev.png",
            alt= "logo",
            class_name="nes-avatar is-large"
        ),
        padding_buttom = Size.BIG.value,
        style=MAX_WIDTH_STYLE,
        align_items= "center"
    )