#!/usr/bin/env python
# coding=utf-8
"""
Created on 2019/5/30

@author: danny.deng
@des: 
"""
import subprocess
import xlwt
import time
from xlwt import Workbook
import os

from config import *

PATH = os.path.abspath(os.path.dirname(__file__))
FILENAME = "ApkPermissionCheck_{}.xls".format(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))


def _run_command(*args):
    """执行aapt命令"""
    rst = ""
    try:
        rst = subprocess.check_output(*args, universal_newlines=True)
    except Exception as e:
        print("error: {}".format(e))
        print("args: {}".format(args))
        exit(1)
    finally:
        return rst


def get_permissions(apk_path):
    """获取apk的所有权限和包名"""
    cmd = ["aapt", "dump", "permissions"]
    cmd.append(apk_path)
    output = _run_command(cmd)
    rst = output.split("\n")
    package_name = ""
    normal_permissions, illegal_permissions, unknown_permissions = [], [], []
    for i in range(len(rst)):
        try:
            item = rst[i].split(":")[1].strip()
        except:
            continue
        if i == 0:
            package_name = item
        elif item in ILLEGAL_PERMISSIONS:
            illegal_permissions.append(item)
        elif item in NORMAL_PERMISSIONS:
            normal_permissions.append(item)
        else:
            unknown_permissions.append(item)
    normal_permissions = "\n".join(normal_permissions)
    illegal_permissions = "\n".join(illegal_permissions)
    unknown_permissions = "\n".join(unknown_permissions)
    return package_name, normal_permissions, illegal_permissions, unknown_permissions


def write_xls(info: dict):
    """
    将权限写文件
    :param info: (dict) key为路径，value为包名和权限
    """
    wb = Workbook()
    st = wb.add_sheet("权限展示")
    st = init_header(st, header_style())
    style = content_style()
    cur_row = 1
    for k, v in info.items():
        st.write(cur_row, 0, k, style)
        st.write(cur_row, 1, v[0], style)
        st.write(cur_row, 2, v[1], style)
        st.write(cur_row, 3, v[2], style)
        st.write(cur_row, 4, v[3], style)
        cur_row += 1
    try:
        fname = os.path.join(PATH, FILENAME)
        wb.save(fname)
    except Exception as e:
        print(str(e))
        print("Error: exception while save excel file.  " + fname)


def content_style():
    """设置样式"""
    font = xlwt.Font()
    font.name = 'Times New Roman'
    font.height = 12 * 20  # font.height = 12 * 20，12号的字体
    # font.underline = True
    # font.italic = True
    content_style = xlwt.XFStyle()
    content_style.font = font
    content_style.font.bold = False
    content_style.alignment.horz = xlwt.Alignment.HORZ_LEFT
    content_style.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
    content_style.alignment.vert = xlwt.Alignment.VERT_CENTER
    return content_style


def header_style():
    font = xlwt.Font()  # 为样式创建字体
    font.name = 'Times New Roman'
    font.height = 13 * 20  # font.height = 12 * 20，12号的字体

    style = xlwt.XFStyle()
    style.font = font
    style.font.bold = True
    style.alignment.horz = xlwt.Alignment.HORZ_CENTER
    style.pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    style.pattern.pattern_fore_colour = 5
    return style


def init_header(sheet, style):
    sheet.col(0).width = 36 * 256  # 路径
    sheet.col(1).width = 36 * 256  # 包名
    sheet.col(2).width = 60 * 256  # 正常权限
    sheet.col(3).width = 60 * 256  # 异常权限
    sheet.col(4).width = 60 * 256  # 未知权限

    sheet.write(0, 0, 'Path', style)
    sheet.write(0, 1, 'PackageName', style)
    sheet.write(0, 2, 'Normal', style)
    sheet.write(0, 3, 'Sensitive', style)
    sheet.write(0, 4, 'Unknown', style)
    return sheet


def walk_dir(root_dir: str) -> list:
    """遍历获得所有apk文件"""
    apk_list = []
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if f.endswith("apk"):
                p = os.path.join(root, f)
                # 兼容pyinstaller
                p = p.replace("\\", "/")
                apk_list.append(p)
    return apk_list


if __name__ == '__main__':
    # print(walk_dir(r"\\192.168.2.123\休闲游戏\Kyuktu"))
    p, ps = get_permissions(
        r"\\192.168.2.123\休闲游戏\Kyuktu\v1.0.2_s1.5.1-382100\AB0S0N00000\general\kyuktu-3_v1.0.2_s1.5.1-382100_AB0S0N00000.apk")
    print(p)
    print(ps)
