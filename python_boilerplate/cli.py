# -*- coding: utf-8 -*-

import sys
from .core import add
#from core import add, subs
from optparse import OptionParser
from . import __version__ as version
#import __version__ as version
from symbol import subscript

def parse_option():
    usage = '%prog num1 num2'

    parser = OptionParser(usage=usage, version=version.__version__)
    return parser.parse_args()

def main():
    option, args = parse_option()
    if len(sys.argv) == 3:
        x, y = map(float, sys.argv[1:])
        print("addition: ", add(x, y))
        print("substraction: ", subs(x, y))
    else:
        print('please specify 2 arguments', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
