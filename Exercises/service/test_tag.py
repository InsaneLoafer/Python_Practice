#!/user/bin/env python
# -*- coding: utf-8 -*-

from Exercises.service.tag import Tag


def test_tag_get():
    tag = Tag()
    token = tag.get_token()

    """获取标签列表"""
    r = tag.list()
    assert r.status_code == 200
    assert r.json()["errcode"] == 0

    """创建标签"""
    res = tag.add(group_name="group1", tags=[{"name": "tag1"}])
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    """校验列表"""
    r = tag.list()
    assert r.status_code == 200
    assert r.json()["errcode"] == 0