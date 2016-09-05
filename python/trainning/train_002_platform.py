#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__='baidw'

import platform
import subprocess
import os

if __name__ == '__main__':
    #print platform.system()
    os_sys = platform.system()
    #print platform.platform()
    #print platform.release()
    #print platform.version()
    #print platform.architecture()
    #print platform.machine()
    print os_sys
