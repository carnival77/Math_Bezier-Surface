#!/usr/bin/env python3

import sys

HELP_MESSAGE = """USAGE
\t./309pollution n file x y

DESCRIPTION
\t n \t number of points on the grid axis
\t file \t csv file containing the data points x;y;p
\t x \t abscissa of the point whose pollution level we want to know
\t y \t ordinate of the point whose pollution level we want to know
"""

def help():
    return HELP_MESSAGE


def error(message):
    sys.stderr.write(message+'\n')
    sys.exit(84)