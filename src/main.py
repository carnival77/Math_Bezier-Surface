#!/usr/bin/env python3

import sys
sys.path.append("src/")
import utils
import func

def main():
    argc = len(sys.argv)
    if argc == 2 and sys.argv[1] == '-h':
            print(utils.help())
            sys.exit(0)
    elif argc == 5:
        try:
            n = int(sys.argv[1])
            csvfile = sys.argv[2]
            px = float(sys.argv[3])
            py = float(sys.argv[4])

            if n <= 0:
                utils.error('Matrix must be > 0.')
            if 0 < px >= n:
                utils.error('Number must be inside the matrix.')
            if 0 < py >= n:
                utils.error('Number must be inside the matrix.')
        except ValueError:
            utils.error('Size must be integer and point must be floats.')
        
    else:
        utils.error('Missing command line argument.')
    #TODO: Check file
    

    matrix = func.fileToMatrix(n, csvfile)
    if matrix == None:
         utils.error('File error.')
    #End of error checking
    


if __name__ == '__main__':
    main()
