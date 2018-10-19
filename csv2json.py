#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2018年10月18日下午09:39:41
@author: songjie
'''
import sys, json, codecs, copy

query = sys.argv[1]


def Csv2Json(file_path):
    # 获取输入数据
    lines = codecs.open(file_path, 'r+', encoding='utf-8').readlines()
    lines = [line.strip() for line in lines]

    line_num = 2
    total_lines = len(lines)

    result = []
    while line_num < total_lines:
        values = lines[line_num].split(",")
        tmp = {}
        tmp["name"] = values[0]
        tmp["children"] = values[1:]
        result = append_line(values, result)
        line_num = line_num + 1

    json_str = json.dumps(result)
    return json_str


def append_line(values, datas):
    tmpdatas = copy.deepcopy(datas)
    valarray = copy.deepcopy(values[1:])
    keyname = values[0]
    if len(tmpdatas) == 0 and keyname:
        tmp = {"name": values[0], "itemStyle": {}}
        if len(values) > 1 and valarray:
            tmp["children"] = append_line(valarray, [])
        tmpdatas.append(tmp)
    else:
        flag = True
        for item in tmpdatas:
            if item["name"] == values[0]:
                flag = False
                children = []
                if item.has_key('children'):
                    children = item["children"]
                tmp = {"name": values[0], "itemStyle": {}}
                if len(values) > 1 and valarray:
                    item["children"] = append_line(valarray, children)
                children.append(tmp)

        if flag and keyname:
            tmp = {}
            tmp["name"] = values[0]
            tmp["itemStyle"] = {}
            if valarray:
                tmp["children"] = append_line(valarray, [])
            tmpdatas.append(tmp)
    return tmpdatas


json_data = Csv2Json(query)
sys.stdout.write(json_data)
