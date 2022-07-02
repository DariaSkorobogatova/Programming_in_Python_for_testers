# -*- coding: utf-8 -*-
from model.group import Group



def test_add_group(app):

   # app.open_home_page()
    app.session.login(username="admin", password="secret")
    #app.group.open_groups_page()
    app.group.create_group(Group(name="kfjdgd", header="asd,fn", footer="s,dfgn"))
    #app.group.return_to_groups_page()
    app.session.logout()


def test_add_empty_group(app):
    #app.open_home_page()
    app.session.login(username="admin", password="secret")
    #app.group.open_groups_page()
    app.group.create_group(Group(name="", header="", footer=""))
    #app.group.return_to_groups_page()
    app.session.logout()


