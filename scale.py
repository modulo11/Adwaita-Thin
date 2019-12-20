import sys, re

GTK_CSS_FILE = sys.argv[1]
NO_SCALE = 1.0
SMALL_SCALE = 0.8
DEFAULT_SCALE = 0.5
ELEMENTS = ['min-height','min-width', 'margin-top', 'margin-bottom', 'margin-left', 'margin-right', 'padding-left', 'padding-right', 'padding-top', 'padding-bottom']

def isLineIgnored(line):
    return line.startswith('switch') or line.startswith('placessidebar') or 'radio' in line

def getScale(line):
    if line.startswith('switch') or 'radio' in line:
        return NO_SCALE
    elif line.startswith('placessidebar'):
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
