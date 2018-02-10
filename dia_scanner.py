import sys
from dia_scanner import diascanner

__author__ = 'kfbBjoern'

def main(*args):
    myScanner = diascanner.DiaScanner('config/Praximat.xml', 10)
    myScanner.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
