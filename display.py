#https://luma-oled.readthedocs.io/en/latest/python-usage.html

from luma.core.interface.serial import i2c
from luma.core.render import canvas 
from luma.oled.device import ssd1306
from PIL import ImageFont

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

font = ImageFont.load_default()

def show_num(value):
    with canvas(device) as draw:
        draw.text((0, 0), str(value), font=font, fill="white")
