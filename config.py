#!/usr/bin/env python
# coding=utf-8
"""
Created on 2019/5/30

@author: danny.deng
@des: 
"""

# 敏感权限
ILLEGAL_PERMISSIONS = [
    'android.permission.RECEIVE_SMS',
    'android.permission.READ_SMS',
    'android.permission.SEND_SMS',
    'android.permission.WRITE_CALENDAR',
    'android.permission.RECORD_AUDIO',
    'android.permission.GET_ACCOUNTS',
    'android.permission.READ_CALENDAR',
    'android.permission.RECEIVE_BOOT_COMPLETED',
    'android.permission.BLUETOOTH',
    'android.permission.BLUETOOTH_ADMIN',
    'android.permission.READ_CONTACTS',
    'android.permission.WRITE_CONTACTS',
    'android.permission.INTERACT_ACROSS_USERS_FULL',
    'android.permission.CAMERA',

]

# 正常权限
NORMAL_PERMISSIONS = [

]