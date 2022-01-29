from client import Webclient

class Test:

    client = Webclient()

    @classmethod
    def setup_class(cls):
        cls.client.start_page.open_page()

    @classmethod
    def teardown_class(cls):
        cls.client.start_page.quit()

    def test(self):
        self.client.start_page.click_dive()
        self.client.start_page.print_list()
        self.client.start_page.click_agency()
        self.client.start_page.show_all()
        self.client.start_page.print_individ_invest()
        self.client.start_page.click_uii_0004()
        self.client.start_page.click_download()
        self.client.start_page.back()
        self.client.start_page.back()
        self.client.start_page.show_all()
        self.client.start_page.click_uii_1327()
        self.client.start_page.click_download()
        self.client.start_page.back()
        self.client.start_page.back()
        self.client.start_page.show_all()
        self.client.start_page.click_uii_1328()
        self.client.start_page.click_download()




