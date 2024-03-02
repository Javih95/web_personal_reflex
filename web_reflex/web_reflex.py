import reflex as rx
import  web_reflex.styles.styles as styles
from web_reflex.views.navBar import navbar
from web_reflex.views.header import header
from web_reflex.views.footer import footer
from web_reflex.styles.styles import Size

def index() -> rx.Component: 
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                footer(),
                width = "100%",
                spacing = Size.VERY_BIG.value
            )
        )
    )



app = rx.App(
    stylesheets= styles.STYLESHEETS,
    style= styles.BASE_STYLE

)
app.add_page(
    index,
    title="CtrlJ - Desarrollador de Software",
    description="Bienvenido a mi espacio digital, donde la creatividad y la pasión se encuentran con el código. Soy CtrlJ, un desarrollador de software con un enfoque único en la creación de soluciones innovadoras. Explora mi portafolio para descubrir proyectos emocionantes, conoce mis habilidades técnicas y únete a mí en el viaje de la programación. ¡Transformemos ideas en realidad!",

)
app.compile()