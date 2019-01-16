#! /usr/bin/python
# -*- coding:utf-8 -*-

import cProfile
import time
def perforance():
    while True:
        time.sleep(1)

if __name__ == '__main__':
    cProfile.run('performance')
