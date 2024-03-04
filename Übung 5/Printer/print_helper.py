from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

def print_color(text, color):
    color_code = {
        "black": "\033[0;30m",
        "red": "\033[0;31m",
        "green": "\033[0;32m",
        "yellow": "\033[0;33m",
        "blue": "\033[0;34m",
        "magenta": "\033[0;35m",
        "cyan": "\033[0;36m",
        "white": "\033[0;37m",
        "bright_black": "\033[0;90m",
        "bright_red": "\033[0;91m",
        "bright_green": "\033[0;92m",
        "bright_yellow": "\033[0;93m",
        "bright_blue": "\033[0;94m",
        "bright_magenta": "\033[0;95m",
        "bright_cyan": "\033[0;96m",
        "bright_white": "\033[0;97m",
    }

    print(color_code[color] + text + "\033[0m")

def print_on_page(letter, color, folder):
    color_code = {"white": (255, 255, 255),
                  "black": (0,0,0),
                  "red": (255, 0, 0),
                  "blue": (0, 0, 255),
                  "green": (0, 255, 0),
                  "yellow": (255, 255, 0)}

    img = Image.new('RGB', (100, 100))
    d = ImageDraw.Draw(img)
    font_path = Path(__file__).parent / "arial.ttf"
    font = ImageFont.truetype(str(font_path), size=80)
    d.text((10, 10), letter, fill=color_code[color], font=font)
    
    folder = Path(folder)
    if not folder.exists():
        folder.mkdir()
    count = len(list(folder.glob("letter*")))
    img.save(folder / f"letter_{count}.png")
