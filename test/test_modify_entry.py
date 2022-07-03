from model.entry import Entry


def test_modify_entry_firstname(app):
    app.session.login(username="admin", password="secret")
    app.entry.modify_entry_firstname(Entry(firstname="Farrokh"))
    app.session.logout()

