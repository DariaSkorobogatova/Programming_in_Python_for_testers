from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.entry import EntryHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.entry = EntryHelper(self)

    def open_home_page(self):
        wd = self.wd
        if not wd.current_url == "https://localhost/addressbook/":
            wd.get("https://localhost/addressbook/")

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

