# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="kfjdgd", header="asd,fn", footer="s,dfgn"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))



