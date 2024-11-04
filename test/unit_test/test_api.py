from unittest import TestCase


class ApiTest(TestCase):
    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.url = ""
        self.user_id = ""
        self.password = ""
        self.db_session = ""

    def test_join(self):
        pass

    def test_login(self):
        pass

    def test_search(self):
        pass

    def get_restorant_data(self):
        pass

    def add_tag(self):
        pass

    def del_tag(self):
        pass

    def change_tag(self):
        pass
