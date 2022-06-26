# -*- coding: utf-8 -*-
import pytest
from model.entry import Entry
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_entry(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.entry.init_entry_creation()
    app.entry.create_entry(Entry(firstname="Freddie", middlename="Queen", lastname="Mercury", nickname="Queen",
    title="Singer", company="Queen", address="London, England", mobile="8888888888", bday="5",
    bmonth="September", byear="1946"))
    app.entry.return_to_home_page()
    app.session.logout()









