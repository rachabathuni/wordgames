import sys

_HEADER = '\033[95m'
_OKBLUE = '\033[94m'
_OKCYAN = '\033[96m'
_OKGREEN = '\033[92m'
_WARNING = '\033[93m'
_FAIL = '\033[91m'
_ENDC = '\033[0m'
_BOLD = '\033[1m'
_UNDERLINE = '\033[4m'

NORMAL = 0x00 
BLUE = 0x01
CYAN = 0x02
GREEN = 0x03
YELLOW = 0x04
RED = 0x05
BOLD = 0x10
UNDERLINE = 0x20

_color_mapping = ["", _OKBLUE, _OKCYAN, _OKGREEN, _WARNING, _FAIL]
_style_mapping = ["", _BOLD, _UNDERLINE]

class ColorPart:
    def __init__(self, text, color):
        self._text = text
        self._color = color


def _get_color_string(msg, color):
    color_code = _color_mapping[color & 0x0F]
    style_code = _style_mapping[color >> 4]
    return f"{color_code}{style_code}{msg}{_ENDC}"

def _cwrite(msg, color):
    if color:
        sys.stdout.write(_get_color_string(msg, color))
    else:
        sys.stdout.write(msg)

def cprint(msg, color):
    _cwrite(msg, color)
    print("")

def cprint_multi(colorparts):
    for part in colorparts:
        _cwrite(part._text, part._color)
    print("")


