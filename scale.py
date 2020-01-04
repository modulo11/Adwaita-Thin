import sys, re

GTK_CSS_FILE = sys.argv[1]
NO_SCALE = 1.0
SMALL_SCALE = 0.7
DEFAULT_SCALE = 0.5
ELEMENTS = ['min-height','min-width', 'margin', 'margin-top', 'margin-bottom', 'margin-left', 'margin-right', 'padding', 'padding-left', 'padding-right', 'padding-top', 'padding-bottom']

def getScale(line):
    if 'radio' in line or 'slider' in line or 'scrollbar' in line:
        return NO_SCALE
    elif line.startswith('switch') or line.startswith('placessidebar') or 'button.titlebutton' in line:
        return SMALL_SCALE
    else:
        return DEFAULT_SCALE

with open(GTK_CSS_FILE, 'r') as f:
    for line in f:
        for element in ELEMENTS:
            if element in line:
                match = re.match('(.*)' + element +': (\w+)px(.*)', line)
                if match:
                    pixel = int(match.group(2))
                    scale = getScale(line)
                    line = line.replace(element + ': ' + match.group(2), element + ': ' + str(int(pixel * scale)))
        print(line, end='')
