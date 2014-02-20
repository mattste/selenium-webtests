# -*- coding: utf-8 -*-

from seleniumwebtests.testcase import *

class homepage(TestCase):

    def test_vyhledavani(self):
        self.driver.get("/")
        search_form = self.driver.find_element_by_id("inet-f")
        self.driver.fill_form_and_submit(search_form, {"q": u"kotě v botě"})
        self.assertIsNotNone(self.driver.find_element_by_id("hledani-seznam-cz"))
