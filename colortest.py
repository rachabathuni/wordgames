#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import colorprint

part1 = colorprint.ColorPart("Hello ", None)
part2 = colorprint.ColorPart("Sailesh", colorprint.RED)

#colorprint.cprint("Hello", colorprint.RED + colorprint.BOLD)
colorprint.cprint_multi([part1, part2])

