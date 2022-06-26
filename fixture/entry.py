class EntryHelper:
    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create_entry(self, entry):
        wd = self.app.wd
        # fill entry's fields
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(entry.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(entry.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(entry.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(entry.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(entry.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(entry.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(entry.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(entry.mobile)
        wd.find_element_by_name("bday").click()
        #Select(wd.find_element_by_name("bday")).select_by_visible_text(entry.bday)
        wd.find_element_by_xpath("//option[@value='" + entry.bday + "']").click()
        wd.find_element_by_name("bmonth").click()
        #Select(wd.find_element_by_name("bmonth")).select_by_visible_text(entry.bmonth)
        wd.find_element_by_xpath("//option[@value='" + entry.bmonth + "']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(entry.byear)
        # submit entry creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def init_entry_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()