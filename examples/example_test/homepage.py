# -*- coding: utf-8 -*-

from seleniumwebtests.testcase import *

class homepage(TestCase):

    def test_vyhledavani(self):
        self.driver.get("/")
        search_form = self.driver.find_element_by_id("inet-f")
        self.driver.fill_form_and_submit(search_form, {"q": u"kotě v botě"})
        self.assertTrue(len(self.driver.find_elements_by_css_selector("#hledani-seznam-cz")) > 0)
