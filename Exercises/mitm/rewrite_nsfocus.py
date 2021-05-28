#!/user/bin/env python
# -*- coding: utf-8 -*-

from mitmproxy import http
import json
from jsonpath import jsonpath

def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if "eventtypesdistr" in flow.request.pretty_url:
        # 将响应内容转成字典格式
        data = json.loads(flow.response.content)
        print(data)
        # 修改对应字段的值
        data[0]['name'] = "SD FLOOD"
        # 把修改后的数据转成字符串赋值给原始数据,text是二进制的流格式也就是原始格式
        flow.response.text = json.dumps(data)