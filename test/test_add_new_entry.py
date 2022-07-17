# -*- coding: utf-8 -*-
from model.entry import Entry


def test_add_new_entry(app):
    old_entries = app.entry.get_entry_list()
    app.entry.create_entry(Entry(firstname="Freddie", middlename="Queen", lastname="Mercury", nickname="Queen",
    title="Singer", company="Queen", address="London, England", mobile="8888888888", bday="5",
    bmonth="September", byear="1946"))
    new_entries = app.entry.get_entry_list()
    assert len(old_entries) + 1 == len(new_entries)








