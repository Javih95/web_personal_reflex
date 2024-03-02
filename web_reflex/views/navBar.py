import reflex as rx
import web_reflex.constantes as constantes
from web_reflex.styles.styles import Size, Color
from web_reflex.components.link_icon import link_icon

def navbar() -> rx.Component: 
    return rx.vstack( 
        rx.hstack(
            rx.image(
                    src="mouredev.png",
                    alt= " Imagen",
                    width =Size.VERY_BIG.value,
                    heigth =Size.VERY_BIG.value
                    ),
            rx.text("CtrlJ - Desarrollador de Software"),
            rx.spacer(),
            link_icon(
                "youtube",
                constantes.YOUTUBE_URL
            ),
            link_icon(
                "github",
                constantes.GITHUB_URL
            ),
            width = "100%"
        ),
        bg = Color.PRIMARIO.value,
        position = "sticky",
        border_bottom = f"0.25em solid {Color.SECUNDARIO.value}",
        padding_x = Size.BIG.value,
        padding_y = Size.DEFAULT.value,
        z_index = "999",
        top ="0",
        width ="100%"

    )