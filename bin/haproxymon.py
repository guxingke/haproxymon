#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: set noet sw=4 ts=4 sts=4 ff=unix fenc=utf8: 

import os
import sys

HMROOT = '/duitang/dist/opt/haproxymon'

sys.path.insert(0, os.path.join(HMROOT, 'lib'))
sys.path.insert(0, os.path.join(HMROOT, 'etc'))

from HaproxyStats import HaproxyStats

if __name__ == "__main__":
    from config import hm_conf
    hs = HaproxyStats(hm_conf)
    hs.sendData()
