import reflex as rx
from .fonts import Font
from.colors import TextColor,Color
from enum import Enum

class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    VERY_BIG = "4em"
    MAX_WIDTH = "1000px"
STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap"
]

BASE_STYLE = {
    "font_family" : Font.DEFAULT.value,
    "color" : TextColor.PRIMARIO.value,
    "background" : Color.PRIMARIO.value,
    rx.Heading:{
        "font_family" : Font.DEFAULT.value,
        "color" : TextColor.DESTACAR.value
    },
    rx.Link:{
        "text_decoration" :"none",
        "_hover" :{
            "color" : TextColor.DESTACAR.value,
            "text_decoration" :"none",
        }
    }
}
MAX_WIDTH_STYLE = dict(
    align_items="start",
    padding_x = Size.BIG.value,
    max_width = Size.MAX_WIDTH.value
)