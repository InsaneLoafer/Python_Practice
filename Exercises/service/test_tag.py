#!/user/bin/env python
# -*- coding: utf-8 -*-
import pytest

from Exercises.service.tag import Tag


# todo: 代码冗余
# todo: 与底层架构耦合太多
# todo: 封装层次不足，不利于管理

class TestTag:

    def setup_class(self):
        # todo: 数据清理过程，把测试数据清空或还原
        self.tag = Tag()
        self.tag.get_token()

    def test_tag_list(self):
        """获取标签列表"""
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

    @pytest.mark.parametrize("group_name, tag_names", [
        ["group1", [{"name": "tag1"}]],
        ["group2", [{"name": "tag2"}, {"name": "tag3"}]]
    ])
    def test_tag_get(self, group_name, tag_names):
        # todo: 完善功能测试
        """创建标签"""
        r = self.tag.add(group_name=group_name, tags=tag_names)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        """校验列表"""
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        group = [group for group in r.json()["tag_group"] if group["group_name"] == group_name][0]
        tags = [{"name": tag['name']} for tag in r.json()["tag"]]
        print(group)
        print(tags)
        assert group['group_name'] == group_name
        assert tags == tag_names

    def test_tag_fail(self):
        pass
