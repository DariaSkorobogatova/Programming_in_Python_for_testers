from model.entry import Entry


def test_delete_first_entry(app):
    if app.entry.count() == 0:
        app.entry.create_entry(Entry(firstname="Freddie", middlename="Queen", lastname="Mercury", nickname="Queen",
                                     title="Singer", company="Queen", address="London, England", mobile="8888888888",
                                     bday="5",
                                     bmonth="September", byear="1946"))
    old_entries = app.entry.get_entry_list()
    app.entry.delete_first_entry()
    new_entries = app.entry.get_entry_list()
    assert len(old_entries) - 1 == len(new_entries)

