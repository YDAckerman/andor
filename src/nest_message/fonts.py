from bdfparser import Font
import os

script_path = os.path.abspath(os.path.dirname(__file__))
font8_path = os.path.join(script_path, '../../static/fonts/ib8x8u.bdf')
font16_path = os.path.join(script_path, '../../static/fonts/ib16x16u.bdf')

FONT_8 = Font(font8_path)
FONT_16 = Font(font16_path)
