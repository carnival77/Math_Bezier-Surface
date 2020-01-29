#!/usr/bin/env python3

import sys
sys.path.append("src/")
import utils
import func

def main():
    argc = len(sys.argv)
    if argc == 2 and sys.argv[1] == '-h':
            print(utils.help())
    elif argc == 5:
        try:
            if float(sys.argv[1]) < 0 or float(sys.argv[3]) < 0 or float(sys.argv[4]) < 0:
                utils.error('Arguments must be >= 0.')
        except ValueError:
            utils.error('Arguments must be numbers.')
    else:
        utils.error('Missing command line argument.')

        #End of error checking


if __name__ == '__main__':
    main()
