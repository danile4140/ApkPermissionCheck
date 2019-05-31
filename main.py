#!/usr/bin/env python
# coding=utf-8
"""
Created on 2019/5/30

@author: danny.deng
@des: 
"""
import sys

from utils import *

if __name__ == '__main__':

    if len(sys.argv) == 2:
        root_dir = sys.argv[1]
    else:
        print('error params..')
        exit(1)
    try:
        apk_list = walk_dir(root_dir)
        dict_permissions = {}
        # 拿到所有的包体和对应的权限
        for i in apk_list:
            print(" 获取权限：{}\n".format(i))
            pkg_name, apk_normal_permissions, apk_illegal_permissions, apk_unknown_permissions = get_permissions(i)
            dict_permissions[i] = [pkg_name, apk_normal_permissions, apk_illegal_permissions, apk_unknown_permissions]
        print(" 权限获取完毕...\n")
        print(" 开始写入xls...\n")
        write_xls(dict_permissions)
        print(" 权限获取完毕...请查看生成的xlsx文件\n")

    except:
        pass
    finally:
        os.system("pause")