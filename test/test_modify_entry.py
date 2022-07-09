from model.entry import Entry


def test_modify_entry_firstname(app):
    if app.entry.count() == 0:
        app.entry.create_entry(Entry(firstname="Freddie", middlename="Queen", lastname="Mercury", nickname="Queen",
                                     title="Singer", company="Queen", address="London, England", mobile="8888888888",
                                     bday="5",
                                     bmonth="September", byear="1946"))
    app.entry.modify_entry_firstname(Entry(firstname="Farrokh"))


