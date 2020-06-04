#!/usr/bin/env python3
"""
Import packages
"""
import sys
from roman import Roman

if __name__ == '__main__':

    try:
        if len(sys.argv) <= 1:
            print("Integer number required")
        else:
            print(Roman().num_roman(int(sys.argv[1])))
    except Exception as e:
        print('Non integers can not be converted')
