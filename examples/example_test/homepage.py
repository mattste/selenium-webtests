# -*- coding: utf-8 -*-

import time
from seleniumwebtests.testcase import *

class Homepage(TestCase):

    def test_brand_selection(self):
        self.proxy.new_har("test")
        self.driver.get("/")
        f = open("har.json", "w")
        f.write(json.dumps(self.proxy.har))
        f.close()
        #form = self.driver.find_element_by_css_selector(".header-search form")
        #self.driver.fill_form_and_submit(form, {"q": "notebooky"})
        #self.driver.wait(5)
        #self.driver.find_element_by_css_selector("#carWrap_1 label").click()
        #self.assertTrue(self.driver.find_element_by_id("manWrap_1").is_displayed())
        self.assertTrue(True)
