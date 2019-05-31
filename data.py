#!/usr/bin/env python
# coding=utf-8
"""
Created on 2019/5/30

@author: danny.deng
@des: 
"""


class Data:
    """结果data"""
    def __init__(self, apk_path=None, legal_permissions=[], illegal_permissions=[]):
        self.apk_path = apk_path
        self.legal_permissions = legal_permissions
        self.illegal_permissions = illegal_permissions

if __name__ == '__main__':
    pass
