# -*- coding: utf-8 -*-

"""
Provides funcionality for easy form filling.
The code has been taken from "python-webdriverwrapper" module
written by Michal Horejsek (https://github.com/horejsek/python-webdriverwrapper)
"""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class Form():

    def __init__(self, elm):
        self.elm = elm

    def fill_out_and_submit(self, data):
        self.fill_out(data)
        self.elm.submit()

    def fill_out(self, data):
        for elm_name, value in data.items():
            FormElement(self.elm, elm_name).fill_out(value)


class FormElement(object):
    def __init__(self, form_elm, elm_name):
        self.form_elm = form_elm
        self.elm_name = elm_name
        self.elm = None

    def convert_value(self, value):
        if not isinstance(value, (list, tuple)):
            return self._convert_value_to_string(value)

        values = []
        for item in value:
            values.append(self._convert_value_to_string(item))
        return values

    def _convert_value_to_string(self, value):
        if isinstance(value, bool):
            value = str(int(value))
        elif value is None:
            value = str('')
        return value

    def set_elm(self, elm):
        self.elm = elm

    def fill_out(self, value):
        tag_name, elm_type = self.analyze_element()
        method_name = ('fill_%s_%s' % (tag_name, elm_type)).replace('-', '')
        getattr(self, method_name, self.fill_common)(value)

    def analyze_element(self):
        elms = []
        if self.elm:
            elms.append(self.elm)
        else:
            elms = self.form_elm.find_elements_by_name(self.elm_name)

        for elm in elms:
            elm_type = elm.get_attribute('type')
            if elm_type == 'hidden':
                continue
            return elm.tag_name, elm_type
        raise NoSuchElementException(_create_exception_msg(name=self.elm_name))

    def fill_input_checkbox(self, value):
        if isinstance(value, (list, tuple)):
            self.fill_input_checkbox_multiple(value)
        self.fill_input_checkbox_single(value)

    def fill_input_checkbox_single(self, value):
        elm = self.form_elm.find_element_by_xpath('//input[@type="checkbox"][@name="%s"]' % self.elm_name)
        if bool(value) != elm.is_selected():
            elm.click()

    def fill_input_checkbox_multiple(self, value):
        for item in value:
            elm = self.form_elm.find_element_by_xpath('//input[@type="checkbox"][@name="%s"][@value="%s"]' %  (
                self.elm_name,
                self.convert_value(item),
            ))
            elm.click()

    def fill_input_radio(self, value):
        elm = self.form_elm.find_element_by_xpath('//input[@type="radio"][@name="%s"][@value="%s"]' % (
            self.elm_name,
            self.convert_value(value),
        ))
        elm.click()

    def fill_input_file(self, value):
        elm = self.form_elm.find_element_by_name(self.elm_name)
        elm.send_keys(self.convert_value(value))

    def fill_select_selectone(self, value):
        select = self.form_elm.find_element_by_name(self.elm_name)
        select.select_by_value(self.convert_value(value))

    def fill_select_selectmultiple(self, value):
        if not isinstance(value, (list, tuple)):
            value = [value]

        select = self.form_elm.find_element_by_name(self.elm_name)
        select.deselect_all()
        for item in self.convert_value(value):
            select.select_by_value(item)

    def fill_common(self, value):
        elm = self.form_elm.find_element_by_name(self.elm_name)
        elm.clear()
        elm.send_keys(self.convert_value(value))
        elm.send_keys(Keys.TAB)  # Send TAB for losing focus. (Trigger change events.)
