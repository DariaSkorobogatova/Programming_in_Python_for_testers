from model.entry import Entry

class EntryHelper:
    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home page").click()

    def create_entry(self, entry):
        wd = self.app.wd
        self.init_entry_creation()
        self.fill_entry_fields(entry)
        # submit entry creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def fill_entry_fields(self, entry):
        wd = self.app.wd
        self.change_field_value("firstname", entry.firstname)
        self.change_field_value("middlename", entry.middlename)
        self.change_field_value("lastname", entry.lastname)
        self.change_field_value("nickname", entry.nickname)
        self.change_field_value("title", entry.title)
        self.change_field_value("company", entry.company)
        self.change_field_value("address", entry.address)
        self.change_field_value("mobile", entry.mobile)
        self.change_field_bday_bmonth("bday", entry.bday)
        self.change_field_bday_bmonth("bmonth", entry.bmonth)
        self.change_field_value("byear", entry.byear)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_bday_bmonth(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_xpath("//option[@value='" + text + "']").click()

    def modify_entry_firstname(self, new_entry_data):
        wd = self.app.wd
        self.go_main_page()
        self.select_first_entry()
        wd.find_element_by_xpath("//*[@title='Edit']").click()
        self.fill_entry_fields(new_entry_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def go_main_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def delete_first_entry(self):
        wd = self.app.wd
        self.select_first_entry()
        # submit deletion
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def select_first_entry(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def init_entry_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        self.go_main_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_entry_list(self):
        wd = self.app.wd
        self.go_main_page()
        entries = []
        for element in wd.find_elements_by_name("entry"):
            # fio = []
            # for el in element.find_elements_by_tag_name("td"):
            #     fio.append(el.text)
            # textname = fio[2]
            # textlastname = fio[1]
            # fio = []
            fio = element.find_elements_by_tag_name("td")
            textname = fio[2].text
            textlastname = fio[1].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            entries.append(Entry(firstname=textname, lastname=textlastname, id=id))
        return entries

